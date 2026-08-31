---
type: moc
topic: "Architecture"
created: 2026-08-10
updated: 2026-08-10
---

# MOC: Architecture

The built substrate of the method. It covers the layer chain, the source typology with its anchor mechanics, and the document schema, together with the question what the carrier format actually guarantees. Supporting strands hold the note taking tradition the layers inherit, the archival criteria for the plain text substrate, and the documented mechanics and limits of the Obsidian conventions the vault rides on.

- [[30_assertions/card-index-organizes-knowledge-as-addressable-linked-notes]], fixed positions and a maintained reference structure carry the yield of Luhmann's card index.
- [[30_assertions/plain-text-meets-archival-format-criteria]], the archival guidances name openness and independence as criteria and rank structured formats above plain text for published works.
- [[30_assertions/obsidian-stores-notes-as-plain-text-with-rebuildable-derived-state]], notes live in plain Markdown files beside a rebuildable metadata cache.
- [[30_assertions/block-references-address-blocks-as-literal-text-markers]], the block identifier is written into the file itself with a restricted character set.
- [[30_assertions/obsidian-link-registers-map-files-to-files]], the declared types of the link registers provide no level below the file.
- [[30_assertions/block-references-are-specific-to-obsidian]], the vendor states that block references sit outside standard Markdown and work only in Obsidian.

- [[30_assertions/layer-model-assigns-each-layer-its-anchor-form]], the five layers and the anchor form each of them carries.
- [[30_assertions/anchors-are-minted-at-their-own-layer-and-bind-one-layer-down]], the two rules that keep the chain from skipping a layer.
- [[30_assertions/status-ladder-is-machine-enforced-and-takes-the-minimum-of-the-anchors]], how a status rises and why it cannot rise above its foundation.
- [[30_assertions/source-type-follows-storability-and-fixes-the-anchor-form]], storability decides the type, and the type decides the anchor.
- [[30_assertions/output-binds-load-bearing-sentences-by-footnote-and-marks-posits]], the anchor contract of the finished text.
- [[30_assertions/markdown-representation-is-immutable-after-ingest]], why a converted representation is frozen and how a revised source enters.

## Open questions

- Which anchor mechanics would an image or audio source type need?
- By what procedure would a further source type enter whose anchor mechanics the schema does not know?
- Which rule fixes the granularity that decides whether a paragraph is anchor-relevant?
- How is a status lowered afterwards when an anchor later falls to contested?
- Does the immutability of a representation still bind where the conversion itself was faulty?
- What does immutability mean for a data representation, whose anchor is a computation and whose data file can be corrected without moving any anchor?
- Does a block reference survive an edit that moves or rewrites its target, the assumption behind the never edit after ingest rule?
- Does a link whose file resolves but whose block identifier does not count as resolved in the link registers?
- How far do archival rankings geared to published content carry to working material inside a research project?
