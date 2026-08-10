<!-- Translated from the German original; that version remains in the git history. -->

# Field report: the KISUG writing wave as a stress test of the template

As of 2026-08-09. Feedback from the instance `kisug-wissensbasis` (private repository) to the template, after the first complete round of query operation, review-wave bookkeeping and new chapter prose with blind double checking. Case-study details stay anonymizably brief here; the instance journals carry the genesis.

## What the template achieved

**The status ladder enforces honesty, and `E-LADDER` is its most effective error code.** Twenty-seven open ladder errors of the instance could only be resolved by a genuine second machine review; that run found two partial supports and one overreach that had been running along as `validated` for weeks (one assertion turned a source statement of "currently not relevant" into "currently not reachable"). Without the ladder rule this would never have been touched again.

**The blind second review finds authoring errors of the operator himself.** In the same round the blind review checked two freshly created assertions of the supervising session and found three overreaches in its own text (an unanchored denominator, content taken from the non-anchorable open questions section, an inference sentence inside the assertion body). The value of separating production from checking is thereby demonstrated on the operator and does not depend on the weakness of third parties.

**The quotation check chain distinguishes versions.** The comparison against locally obtained full texts found a distillate whose quotations followed the arXiv version while the reference points to the publisher version; two formulations diverged. At the same time a sample taken by the main thread refuted a false finding of the checking agent (an alleged whitespace divergence that the publisher version does not carry). The layering of agent check and main-thread sample catches errors in both directions.

**The provenance chain pays off in query operation.** An overall report across 44 internal sources could be written with a carrier layer per statement, and seven load-bearing findings were verifiable against the distillate anchors within minutes, because every anchor can be addressed directly. An adversarial re-check of the same report found 13 divergences across roughly 215 stated items; that check too was possible only because the anchors exist.

**Chapter prose on a finished assertion layer is fast and stays checkable.** The first new chapter of the instance was produced in one go on 28 existing assertions, and the two blind reviews (anchor fidelity, fact check) together delivered 24 precise, fixable findings. The footnote contract makes the reviews mechanically checkable; no finding was a matter of taste.

## Where the template showed gaps

Every gap is a concrete incident of that day, not a hypothetical risk.

1. **Duplicate detection is missing.** The supervising session created an assertion that already existed with an identical grounding set (four identical anchors); only the blind review found it, and deletion was done by hand. Proposal: a validator or lint check that reports assertion pairs with an identical or nearly identical grounding set as a warning (something like `W-DUPLICATE-GROUNDING`). That is cheap to check and would have caught the case mechanically.
2. **Register drift is invisible.** The status column of the instance's inventory register diverged from the real frontmatter status of the distillates in 36 rows, a silent remainder of earlier bookkeeping waves. Proposal: a check that compares the status entries of the `state` tables against the frontmatter of the linked files (something like `W-REGISTER-DRIFT`).
3. **Alias drift in footnotes.** Nine footnote aliases of the new chapter shortened the assertion titles, in part by exactly the restricting clause; the human-led review found it. Proposal: a lint comparison of the alias text of `Grounded in` footnotes against the H1 title of the target file (a warning on divergence).
4. **The open questions section of the distillates is an anchor shadow.** Findings standing there are not citable, yet they often carry exactly the restrictions an assertion needs; in the instance a statement had to be scaled back for that reason although the content stands in the distillate. Proposal for discussion: either a convention of lifting checkable findings into the core statements by an additive anchor, or a separate anchorable findings section.
5. **Tool paths in instance control documents drift.** The instance CLAUDE.md named a validator path that exists only in the template; it was noticed only by a checking agent. The existing stale-path check of `migrate.py` could be extended to the command lines documented in CLAUDE.md.

## Assessment

After the round the instance stands at four validator errors, all of which trace back to a single source work not yet obtained, at zero lint errors without an undeclared warning, and every load-bearing statement of the new prose is traceable through the chain down to its source location. That the remaining errors map exactly onto the real-world gap (one missing PDF) and onto nothing else is the behaviour the architecture was built for. The five gaps above are tooling gaps at the edge of the chain; the chain itself held in every direction of checking.
