# Template decisions

Decisions about the template itself, with their reasons, newest entry last. The changelog tells an instance what changed and whether it has to act, and the journal of each instance records that instance's own decisions. Neither has room for why the template is shaped as it is, which is what this document holds. An entry records a decision, the alternative it rejected and the reason, in a few sentences.

## 2026-10-03, public example and content-bound review

The public example under `examples/prov-entity/` preserves a selected original excerpt and follows its anchor chain through a reviewed statement to output, so that the complete chain can be inspected without private material. Review judgements are bound to the exact prompt by a digest, the full prose of an assertion's Statement section is paired, ambiguous imports fail, and each check keeps its own freshness, because a validation date must not hide an older review. Template code is MIT and authored text CC BY 4.0, following the author's standing publication instruction.

## 2026-10-04, nested instances copy the invariant documents

The two instances inside this repository, the worked example and the internal manuscript, carry their own copies of index, schema and operations, and `tests/test_instances.py` holds every copy equal to the root apart from the frontmatter values an instantiation fills. The alternative, referencing the root documents from the instance, was in use for the manuscript. It avoided a second copy but left the instance's wikilinks resolving to template documents that still carry placeholders, and it left the root unable to describe an instance with three knowledge documents while calling six invariant. Every external instance is a copy anyway, so the nested ones now behave like them, and the test replaces the discipline a copy otherwise lacks.

## 2026-10-04, the concept paper argues and the knowledge documents rule

`docs/concept.md` carried a second terminology and restated the layer table, the source type rules and the status progression in its own words, and six of those restatements had drifted from `knowledge/`. The paper now holds the problem, the idea, the reasons behind the vocabulary and the architecture, and the lineage, and it points to the knowledge documents for every rule. The alternative, keeping it as a self-contained essay with a precedence note, was rejected because two statements of one rule do not stay equal without a check, and no check can compare prose written in two registers.

## 2026-10-04, template decisions get a document of their own

The root journal is the empty journal an instance starts from, and the changelog is written for instances. Template decisions with their reasons had no place and ended up in the root journal, which every instance inherited. By the split rule the knowledge documents state for themselves, divergent readers and update rhythms justify a document, so this one exists under `docs/`, which an instance may delete.

## 2026-10-04, a self-report anchor gives way to an independent source (revisable)

Where a source speaks about itself, an assertion either carries the speaker along or rests on an independent source. The rule now says that in the second case the self-report anchor is dropped from the grounding. Machine review judges per pair and marks a self-report pair as overreaching whenever the assertion asserts the matter itself, so an assertion that kept both anchors could never reach `validated`. The alternative is a marked secondary anchor that review skips. That would be a new mechanism and would let an unsupported anchor stand in the grounding, so it was not taken, and the choice stays open to revision if the manuscript work shows that the self-report should remain visible as support.

## 2026-10-04, assertion building sets contested and verification resolves it (revisable)

The status `contested` had a definition and a validator rule but no procedure that sets or resolves it. Assertion building is now the only step that sets it, a machine review verdict of *contradicts* sends the pair back to that step, and human verification alone resolves a contested pair by recording in the journal which side holds. The reasons are that the review contract limits machine review to lifting a document to `validated`, and that a contradiction between sources is an evidence question, which the architecture reserves for verification. The alternative, leaving contested pairs standing permanently as information, remains possible by never resolving them, so the rule constrains who may resolve rather than whether.

## 2026-10-04, the migration tool is removed

`tools/migrate.py` carried the folder mappings of two external vaults built before the template chain. Both migrations have run, no control document routed to the tool, and git history keeps it. A template that ships mappings for vaults its users have never seen is heavier than it needs to be.

## 2026-10-04, the source manifest, the notice and the review records become schema

The worked example introduced `manifest.json`, `NOTICE` and `checks/` without the schema knowing them. The manifest makes the hard rule that a Markdown representation is never edited after ingest checkable, which no tool did before, and a hard rule without a check contradicts the principle that status follows from checks that ran. The returned review batches had a contract that allowed them to retain reviewer and date but no place to live. All three are now optional parts of the schema, the manifest with its own finding codes.

## 2026-10-04, four terminology entries carry rules (revisable)

Filling the gaps in the terminology meant deciding four things no document had settled. An anchor-relevant paragraph is one that carries a statement a distillate could reproduce, so headings, captions, table cells, navigation text and boilerplate receive no block ID, because stamping them lowers coverage without adding anything checkable. A load-bearing sentence is one whose claim the chapter would lose if it were struck, which leaves connecting and summarizing sentences free of footnotes. A posit candidate is noted under the open questions of its topic map, the one register the chain already keeps for what the sources leave open. Where verification samples, only the sampled relations are evidence, and `verified` on the document records that the sampling rule in the journal was applied. Each of these could be drawn differently, and an instance that finds one of them wrong should say so in its journal so that the template can follow.

## 2026-10-04, the manifest digest tolerates line-end conversion

The digest of a text file is defined over its content with CRLF folded to LF, and validation also accepts the digest of the raw bytes. Git on Windows converts the line ends of every text file at checkout, so a digest over raw bytes would fail on one platform or the other while the content is unchanged. The cost is that an edit consisting solely of line-end changes passes the check. It changes no block and no anchor, so the rule the manifest protects is not touched by it.

## 2026-10-04, copies are refreshed by a tool

`tools/sync_instances.py` rewrites the knowledge copies of the nested instances from the root and keeps the values the instance filled. The test alone would have left the fix as a manual copy, which is the kind of step that gets done inconsistently. The tool and the test together are the whole discipline the copy model needs.
