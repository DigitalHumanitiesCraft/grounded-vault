"""Reference implementation of the machine review of a Grounded Vault.

Implements the machine-review contract of knowledge/operations.md § Check. The
work splits into three parts that are kept apart on purpose.

1. Pair cutting, deterministic. Every distillate statement is cut against its
   source location (document: the block with its heading path; publication: the
   verbatim quotation; data: the computation and its result), and every
   grounding anchor of an assertion is cut against the distillate statement it
   names. Anti-anchoring is structural here: a pair holds the location, the
   statement built on it and nothing else, so the producing agent's reasoning,
   its Support prose and even the anchors themselves stay out of the prompt.
2. Prompt construction from the skeletons in operations.md, one prompt per pair.
3. Judging, pluggable. The default mode writes the prompts as a JSONL batch and
   reads verdicts back as JSONL, so any reviewer (another model family is
   recommended) can sit in between. `run` calls `claude -p` per pair instead.
   The verdict vocabulary is strict; anything else is a parse error.

Booking is conservative: checked.machine-review is set on a document only when
every one of its pairs came back *fully supports*. Deviating verdicts are
reported and nothing is reformulated automatically.

Usage:
    python tools/review.py stats <vault-root>
    python tools/review.py emit  <vault-root> --out prompts.jsonl
    python tools/review.py judge <vault-root> --verdicts verdicts.jsonl [--apply]
    python tools/review.py run   <vault-root> --model <model> [--apply]

Parsing conventions are imported from tools/validate.py rather than restated.
Validation gates review, so booking under --apply runs the validator first and
books no document that carries a validation error.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from validate import (
    ASSERTION_LAYER,
    BLOCK_ID,
    COMPUTATION,
    DISTILLATE_LAYER,
    H1,
    REPRESENTATION_LAYER,
    WIKILINK,
    Doc,
    field_links,
    link_targets,
    load_docs,
    quotation_text,
    split_frontmatter,
    statement_lines,
    utf8_console,
    validate,
    write_text_atomic,
)

VERDICTS = (
    "fully supports",
    "partially supports",
    "overreaches",
    "contradicts",
    "not in the text",
)
PASSING_VERDICT = "fully supports"

SOURCE_PROMPT = """You are an adversarial reviewer. Below are a source passage and a statement
that claims to be supported by it. Your task is to refute the statement.
Judge only whether this passage supports this statement. Answer with exactly
one verdict: {vocabulary}. Then give one sentence of justification. If the passage
speaks about its own source, or shows its matter in one dated state, the
statement is fully supported only if it keeps the speaker or the state with
its date, and it overreaches otherwise. In either case add one line naming
the displacement.

PASSAGE: {passage}
STATEMENT: {statement}"""

ASSERTION_PROMPT = """You are an adversarial reviewer. Below are a distillate statement and an
assertion that claims to be supported by it. Your task is to refute the
assertion. Judge only whether this statement supports this assertion; whether
the assertion is true is out of scope. Answer with exactly one verdict:
{vocabulary}. Then give one sentence of justification, and where the verdict is
not *fully supports*, name the part of the assertion that the statement does not
carry. If the statement reports what its source says about itself, or shows the
matter in one dated state, the assertion is fully supported only if it keeps the
speaker or the state with its date, and it overreaches otherwise. In either case
add one line naming the displacement.

STATEMENT: {statement}
ASSERTION: {assertion}"""

VERDICT_LINE = re.compile(
    r"^(?:verdict\s*:\s*)?(fully supports|partially supports|overreaches|contradicts|not in the text)[.!]?$",
    re.IGNORECASE,
)
CHECKED_EMPTY = re.compile(r"^checked:[ \t]*\{\s*\}[ \t]*$", re.MULTILINE)
CHECKED_BLOCK = re.compile(r"^checked:[ \t]*$", re.MULTILINE)


@dataclass(frozen=True)
class Pair:
    """One reviewable pair: a location, the statement built on it, nothing else.

    For a source pair the location is the source passage and the statement is
    the distillate statement. For an assertion pair the location is the
    distillate statement and the statement is the assertion sentence, the
    statement built on it in the sense of the machine-review contract.
    """

    id: str
    kind: str  # source | assertion
    document: str  # the document under review, root-relative without extension
    anchor: str  # the anchor that ties statement to location, for the report only
    location: str
    statement: str

    @property
    def prompt(self) -> str:
        return build_prompt(self)

    @property
    def prompt_hash(self) -> str:
        return hashlib.sha256(self.prompt.encode("utf-8")).hexdigest()

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "kind": self.kind,
            "document": self.document,
            "anchor": self.anchor,
            "location": self.location,
            "statement": self.statement,
            "prompt": self.prompt,
            "prompt_hash": self.prompt_hash,
        }


@dataclass(frozen=True)
class Judgement:
    verdict: str
    prompt_hash: str


@dataclass(frozen=True)
class Deviation:
    pair_id: str
    document: str
    verdict: str


@dataclass(frozen=True)
class DocumentResult:
    document: str
    pairs: int
    booked: bool
    reason: str


@dataclass
class Outcome:
    documents: list[DocumentResult] = field(default_factory=list)
    deviations: list[Deviation] = field(default_factory=list)
    unjudged: list[str] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)


def build_prompt(pair: Pair) -> str:
    vocabulary = " | ".join(VERDICTS)
    if pair.kind == "source":
        return SOURCE_PROMPT.format(
            vocabulary=vocabulary, passage=pair.location, statement=pair.statement
        )
    return ASSERTION_PROMPT.format(
        vocabulary=vocabulary, statement=pair.location, assertion=pair.statement
    )


def parse_verdict(response: str) -> str:
    """The verdict vocabulary is closed; anything outside it is a parse error."""
    head = " ".join(response.strip().splitlines()[:1]).strip()
    head = " ".join(head.split())
    # Markdown emphasis may wrap the label or verdict, but does not change it.
    head = head.replace("**", "").replace("__", "").strip("*`_")
    if match := VERDICT_LINE.fullmatch(head):
        return match.group(1).lower()
    raise ValueError(f"no single verdict in response: {response.strip()[:80]!r}")


def _statement_text(line: str) -> str:
    """The bare statement of a bullet, stripped of its anchor and its own ID."""
    text = line.strip()
    text = text[2:] if text.startswith("- ") else text
    text = BLOCK_ID.sub("", WIKILINK.sub("", text).strip())
    return " ".join(text.split())


def _block_locations(doc: Doc) -> dict[str, str]:
    """Per block ID the passage text with the heading path it sits under."""
    stack: list[tuple[int, str]] = []
    paragraph: list[str] = []
    locations: dict[str, str] = {}
    for raw in doc.body.splitlines():
        line = raw.strip()
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, line[level:].strip()))
            paragraph = []
            continue
        if not line:
            paragraph = []
            continue
        paragraph.append(line)
        if m := BLOCK_ID.search(line):
            text = BLOCK_ID.sub("", " ".join(paragraph).strip()).strip()
            path = " > ".join(title for _, title in stack)
            locations[m.group(1)] = f"{path}\n{text}" if path else text
            paragraph = []
    return locations


def _source_pairs(
    doc: Doc,
    blocks: dict[str, dict[str, str]],
    problems: list[str],
) -> list[Pair]:
    source_type = doc.fm.get("source-type")
    pairs: list[Pair] = []
    for line, follow in statement_lines(doc.body):
        m = BLOCK_ID.search(line)
        if not m:
            problems.append(f"{doc.rel}: statement without ID, skipped")
            continue
        sid = m.group(1)
        statement = _statement_text(line)
        anchor, location = "", ""
        if source_type == "document":
            anchored = [(t, b) for t, b in link_targets(line) if b]
            if not anchored:
                problems.append(f"{doc.rel}#^{sid}: no block anchor, skipped")
                continue
            target, block = anchored[0]
            if target not in blocks or block not in blocks[target]:
                problems.append(
                    f"{doc.rel}#^{sid}: anchor {target}#^{block} does not resolve"
                )
                continue
            anchor, location = f"{target}#^{block}", blocks[target][block]
        elif source_type == "publication":
            location = quotation_text(follow)
            if not location:
                problems.append(f"{doc.rel}#^{sid}: no quotation, skipped")
                continue
            anchor = str(doc.fm.get("reference", ""))
        elif source_type == "data":
            declared = [c for f in follow if (c := COMPUTATION.search(f))]
            if not declared:
                problems.append(f"{doc.rel}#^{sid}: no computation, skipped")
                continue
            anchor = declared[0].group(1)
            location = (
                f"computation: `{declared[0].group(1)}` → `{declared[0].group(2)}`"
            )
        else:
            problems.append(f"{doc.rel}: unknown source-type {source_type!r}, skipped")
            return []
        pairs.append(
            Pair(
                id=f"{doc.rel}#^{sid}",
                kind="source",
                document=doc.rel,
                anchor=anchor,
                location=location,
                statement=statement,
            )
        )
    return pairs


def _assertion_pairs(
    doc: Doc, statements: dict[str, str], problems: list[str]
) -> list[Pair]:
    title = H1.search(doc.body)
    sentence = title.group(1).strip() if title else ""
    section = re.search(
        r"^## Statement\s*\n(.*?)(?=^## |\Z)", doc.body, re.MULTILINE | re.DOTALL
    )
    if section:
        sentence = section.group(1).strip()
    if not sentence:
        problems.append(f"{doc.rel}: no assertion statement, skipped")
        return []
    pairs: list[Pair] = []
    for target, block in field_links(doc.fm, "grounding"):
        key = f"{target}#^{block}" if block else target
        if key not in statements:
            problems.append(f"{doc.rel}: grounding {key} does not resolve, skipped")
            continue
        pairs.append(
            Pair(
                id=f"{doc.rel}<-{key}",
                kind="assertion",
                document=doc.rel,
                anchor=key,
                location=statements[key],
                statement=sentence,
            )
        )
    return pairs


def cut_pairs(root: Path, problems: list[str] | None = None) -> list[Pair]:
    """All reviewable pairs of the vault, in document order.

    A document that fails to parse cannot be cut, so its parse finding goes
    into `problems` instead of vanishing with it.
    """
    problems = problems if problems is not None else []
    docs, report = load_docs(
        root, (REPRESENTATION_LAYER, DISTILLATE_LAYER, ASSERTION_LAYER)
    )
    problems += [f"{rel}: {code} {message}" for code, rel, message in report.errors]
    blocks = {
        rel: _block_locations(doc)
        for rel, doc in docs.items()
        if doc.fm.get("type") == "representation"
    }
    pairs: list[Pair] = []
    statements: dict[str, str] = {}
    for rel in sorted(docs):
        doc = docs[rel]
        if doc.fm.get("type") != "distillate":
            continue
        for pair in _source_pairs(doc, blocks, problems):
            pairs.append(pair)
            statements[pair.id] = pair.statement
    for rel in sorted(docs):
        doc = docs[rel]
        if doc.fm.get("type") == "assertion":
            pairs += _assertion_pairs(doc, statements, problems)
    return pairs


def set_checked_date(text: str, check: str, date: str) -> str:
    """Write one entry into the `checked` map of a frontmatter, leaving the rest alone."""
    split = split_frontmatter(text)
    if split is None:
        raise ValueError("no frontmatter")
    # The body follows the closing delimiter, so the frontmatter ends where
    # the delimiter in front of the body begins.
    end = len(text) - len(split[1]) - len("\n---")
    head, tail = text[:end], text[end:]
    entry = re.compile(rf"^([ \t]+){re.escape(check)}:[ \t]*\S.*$", re.MULTILINE)
    if m := entry.search(head):
        return f"{head[: m.start()]}{m.group(1)}{check}: {date}{head[m.end() :]}{tail}"
    if m := CHECKED_EMPTY.search(head):
        return f"{head[: m.start()]}checked:\n  {check}: {date}{head[m.end() :]}{tail}"
    if m := CHECKED_BLOCK.search(head):
        return f"{head[: m.end()]}\n  {check}: {date}{head[m.end() :]}{tail}"
    raise ValueError(f"no checked field to write {check} into")


def book_results(
    root: Path,
    pairs: list[Pair],
    verdicts: dict[str, Judgement],
    date: str,
    apply: bool = False,
) -> Outcome:
    """Set checked.machine-review per document, only where every pair passed.

    Under `apply` the validator runs first, because validation gates every other
    check; a document with a validation error is reported and left unbooked.
    """
    outcome = Outcome()
    try:
        if datetime.date.fromisoformat(date).isoformat() != date:
            raise ValueError
    except (TypeError, ValueError):
        outcome.problems.append("review date must use strict ISO YYYY-MM-DD format")
        return outcome
    by_document: dict[str, list[Pair]] = {}
    for pair in pairs:
        by_document.setdefault(pair.document, []).append(pair)
    if not pairs:
        outcome.problems.append("no reviewable pairs; no machine review took place")
        return outcome
    unknown = set(verdicts) - {pair.id for pair in pairs}
    if unknown:
        outcome.problems += [
            f"unknown verdict id: {pair_id}" for pair_id in sorted(unknown)
        ]
        return outcome
    invalid = {rel for _, rel, _ in validate(root).errors} if apply else set()
    # A caller may hold pairs emitted before another process changed the files.
    current_pairs = cut_pairs(root) if apply else []
    current_hashes = {p.id: p.prompt_hash for p in current_pairs}

    for document, group in by_document.items():
        incomplete = apply and {p.id for p in group} != {
            p.id for p in current_pairs if p.document == document
        }
        if incomplete:
            outcome.problems.append(
                f"{document}: pair set changed; emit and review every current pair"
            )
        missing = [p.id for p in group if p.id not in verdicts]
        outcome.unjudged += missing
        mismatched = [
            p.id
            for p in group
            if p.id in verdicts
            and (
                not isinstance(verdicts[p.id], Judgement)
                or verdicts[p.id].prompt_hash != p.prompt_hash
                or verdicts[p.id].verdict not in VERDICTS
                or (apply and current_hashes.get(p.id) != p.prompt_hash)
            )
        ]
        outcome.problems += [
            f"{pair_id}: unbound or stale verdict; emit and review the current pair"
            for pair_id in mismatched
        ]
        deviating = [
            Deviation(p.id, document, verdicts[p.id].verdict)
            for p in group
            if p.id in verdicts
            and p.id not in mismatched
            and verdicts[p.id].verdict != PASSING_VERDICT
        ]
        outcome.deviations += deviating
        if incomplete:
            reason = "pair set changed after review"
        elif missing:
            reason = f"{len(missing)} pair(s) unjudged"
        elif mismatched:
            reason = f"{len(mismatched)} unbound or stale verdict(s)"
        elif deviating:
            reason = f"{len(deviating)} verdict(s) below {PASSING_VERDICT}"
        else:
            reason = "all pairs fully supports"
        booked = not incomplete and not missing and not mismatched and not deviating
        if booked and document in invalid:
            booked, reason = False, "validation errors, run tools/validate.py"
            outcome.problems.append(f"{document}: not booked: {reason}")
        if booked and apply:
            path = root / f"{document}.md"
            try:
                text = set_checked_date(
                    path.read_text(encoding="utf-8"), "machine-review", date
                )
            except (ValueError, OSError) as exc:
                outcome.problems.append(f"{document}: not booked: {exc}")
                booked, reason = False, str(exc)
            else:
                write_text_atomic(path, text)
        outcome.documents.append(DocumentResult(document, len(group), booked, reason))
    return outcome


def read_verdicts(path: Path, problems: list[str]) -> dict[str, Judgement]:
    """Read judgements bound to the exact emitted prompt by `prompt_hash`."""
    verdicts: dict[str, Judgement] = {}
    seen: set[str] = set()
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
            if not isinstance(record, dict):
                raise ValueError("verdict record must be a JSON object")
            pair_id = record["id"]
            if not isinstance(pair_id, str) or not pair_id:
                raise ValueError("verdict id must be a nonempty string")
            if pair_id in seen:
                verdicts.pop(pair_id, None)
                raise ValueError(f"duplicate verdict id: {pair_id}")
            seen.add(pair_id)
            prompt_hash = record["prompt_hash"]
            if not isinstance(prompt_hash, str) or not re.fullmatch(
                r"[0-9a-f]{64}", prompt_hash
            ):
                raise ValueError("prompt_hash must be the emitted SHA-256 digest")
            verdict = parse_verdict(record.get("verdict") or record["response"])
            if (
                record.get("verdict")
                and record.get("response")
                and parse_verdict(record["response"]) != verdict
            ):
                raise ValueError("verdict and response conflict")
            verdicts[pair_id] = Judgement(verdict, prompt_hash)
        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
            AttributeError,
        ) as exc:
            problems.append(f"{path}:{number}: {exc}")
    return verdicts


def run_claude(
    pairs: list[Pair], model: str | None, problems: list[str], timeout: int = 300
) -> list[dict[str, str]]:
    """Judge each pair with `claude -p` as a subprocess, one call per pair.

    The prompt goes in on stdin; a command line caps out around 32k characters on
    Windows, and a quotation with its heading path can pass that.
    """
    executable = shutil.which("claude")
    if not executable:
        raise RuntimeError("claude executable not found on PATH")
    records: list[dict[str, str]] = []
    for pair in pairs:
        command = [executable, "-p"]
        if model:
            command += ["--model", model]
        try:
            result = subprocess.run(
                command,
                input=pair.prompt,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired:
            problems.append(f"{pair.id}: judging timed out after {timeout}s")
            continue
        if result.returncode != 0:
            problems.append(f"{pair.id}: claude failed: {result.stderr.strip()[:120]}")
            continue
        record = {
            "id": pair.id,
            "prompt_hash": pair.prompt_hash,
            "response": result.stdout.strip(),
        }
        if model:
            record["model"] = model
        try:
            record["verdict"] = parse_verdict(result.stdout)
        except ValueError as exc:
            problems.append(f"{pair.id}: {exc}")
        records.append(record)
        print(f"OK {pair.id}: {record.get('verdict', 'unparsed')}")
    return records


def _select(pairs: list[Pair], scope: str, prefix: str | None) -> list[Pair]:
    chosen = [p for p in pairs if scope == "all" or p.kind == scope]
    return [p for p in chosen if not prefix or p.document.startswith(prefix)]


def _write_jsonl(path: Path | None, records: list[dict[str, str]]) -> None:
    lines = [json.dumps(record, ensure_ascii=False) for record in records]
    if path is None:
        print("\n".join(lines))
        return
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"OK {len(records)} record(s) written to {path}")


def _report(outcome: Outcome, pairs: list[Pair]) -> int:
    for problem in outcome.problems:
        print(f"WARN {problem}", file=sys.stderr)
    for deviation in outcome.deviations:
        print(
            f"FINDING {deviation.verdict}: {deviation.pair_id}",
            file=sys.stderr,
        )
    for pair_id in outcome.unjudged:
        print(f"OPEN no verdict: {pair_id}", file=sys.stderr)
    booked = [r for r in outcome.documents if r.booked]
    print(
        f"{len(pairs)} pair(s), {len(booked)} of {len(outcome.documents)} document(s) clean, "
        f"{len(outcome.deviations)} deviating verdict(s), {len(outcome.unjudged)} unjudged"
    )
    for result in outcome.documents:
        mark = " " if result.booked else "*"
        print(f"{mark} {result.document}: {result.pairs} pair(s), {result.reason}")
    return 1 if outcome.deviations or outcome.unjudged or outcome.problems else 0


def main() -> int:
    utf8_console()
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("root", type=Path, help="vault root directory")
    common.add_argument(
        "--scope",
        choices=("all", "source", "assertion"),
        default="all",
        help="which pair kind to review",
    )
    common.add_argument(
        "--path", help="restrict to documents whose path starts with this prefix"
    )
    booking = argparse.ArgumentParser(add_help=False)
    booking.add_argument(
        "--apply",
        action="store_true",
        help="write checked.machine-review; default is a dry run",
    )
    booking.add_argument(
        "--date",
        default=datetime.date.today().isoformat(),
        help="date recorded in checked.machine-review",
    )

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("stats", parents=[common], help="count the pairs without judging")
    emit = sub.add_parser(
        "emit", parents=[common], help="write the prompts as a JSONL batch"
    )
    emit.add_argument("--out", type=Path, help="output file; default is stdout")
    judge = sub.add_parser(
        "judge",
        parents=[common, booking],
        help="read verdicts back and book the result",
    )
    judge.add_argument(
        "--verdicts",
        type=Path,
        required=True,
        help="JSONL of judgements with id, prompt_hash and verdict or response",
    )
    run = sub.add_parser(
        "run",
        parents=[common, booking],
        help="judge with `claude -p`, one call per pair",
    )
    run.add_argument("--model", help="model passed to claude -p")
    run.add_argument("--out", type=Path, help="write the judgements as JSONL as well")
    args = parser.parse_args()

    root = args.root.resolve()
    problems: list[str] = []
    pairs = _select(cut_pairs(root, problems), args.scope, args.path)

    if args.command != "stats" and not pairs:
        return _report(
            Outcome(
                problems=[
                    *problems,
                    "no reviewable pairs; no machine review took place",
                ]
            ),
            pairs,
        )

    if args.command == "stats":
        kinds = {
            kind: sum(p.kind == kind for p in pairs) for kind in ("source", "assertion")
        }
        documents = {p.document for p in pairs}
        print(f"{len(pairs)} pair(s) over {len(documents)} document(s): {kinds}")
    elif args.command == "emit":
        _write_jsonl(args.out, [p.to_dict() for p in pairs])
    elif args.command == "judge":
        verdicts = read_verdicts(args.verdicts, problems)
        if problems:
            return _report(Outcome(problems=problems), pairs)
        outcome = book_results(root, pairs, verdicts, args.date, apply=args.apply)
        outcome.problems = problems + outcome.problems
        return _report(outcome, pairs)
    elif args.command == "run":
        records = run_claude(pairs, args.model, problems)
        if args.out:
            _write_jsonl(args.out, records)
        verdicts = {
            r["id"]: Judgement(r["verdict"], r["prompt_hash"])
            for r in records
            if "verdict" in r
        }
        if problems:
            return _report(Outcome(problems=problems), pairs)
        outcome = book_results(root, pairs, verdicts, args.date, apply=args.apply)
        outcome.problems = problems + outcome.problems
        return _report(outcome, pairs)

    for problem in problems:
        print(f"WARN {problem}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
