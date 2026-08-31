---
type: distillate
source-type: document
representation: "[[10_markdown/documents/dpc-handbook-file-formats-and-standards]]"
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: DPC Digital Preservation Handbook, File formats and standards

The Digital Preservation Coalition names the factors to weigh when choosing a preservation format, and puts proliferation of formats alongside obsolescence as the risk a strategy has to answer.

## Core statements

- A preservation strategy should move towards simple and practical actions rather than trying to support more file formats than an organisation needs. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-01]] ^s1
- Migration is a valid and, for many file formats, common preservation strategy, but it is not the only approach or solution. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-03]] ^s2
- Both open source and commercial formats are vulnerable to obsolescence, because vendors sometimes use planned obsolescence to drive upgrades, open source communities may withdraw support for formats they no longer need, and both businesses and communities can fail. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-06]] ^s3
- File format obsolescence is a risk that needs to be understood, but it may be less severe than the digital preservation community perceived it a decade earlier, since many established formats remain supported and usable. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-07]] ^s4
- Arguably, in some sectors proliferation is more of a challenge than obsolescence, since an organisation that does not normalise can end up with many formats and versions whose risks and tools become hard to track. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-08]] ^s5
- Not all digital formats are suited or designed for archiving, so a preservation policy should recognise the requirements of the collection content and decide on the format that best preserves those qualities. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-10]] ^s6
- The choice between open source and proprietary formats is not simple, because proprietary formats such as TIFF are seen as robust yet remain susceptible to obsolescence if their owner fails or moves on, while open source formats can be seen as technologically neutral and also vulnerable to the susceptibilities of the communities that support them. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-11]] ^s7
- Where only proprietary formats are available for an application area, a crucial factor is which export formats are supported, so that data can be moved out of or into the proprietary environment. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-12]] ^s8
- The availability of documentation such as published specifications is an important factor in selecting a file format, and the standard chosen should be well-documented, widely implemented and listed in the PRONOM registry. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-13]] ^s9
- A format relied upon by a large user group creates more options for its users, and wide adoption of a format can give more confidence in a preservation strategy. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-14]] ^s10
- One rule of thumb is to choose lossless formats for creating and storing archival masters and to use lossy formats only for delivery or access, not as archival copies. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-17]] ^s11
- Some file formats allow metadata to be inscribed directly into an instance of a file, which can be a consideration depending on the approach taken to metadata management. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-18]] ^s12
- One view regards significant properties as the essence of file content, which permits a strategy of preserving only those aspects of a format that carry the most meaning and value to the user rather than all of them. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-19]] ^s13
- Significant properties may also be technical metadata required for a file to be rendered, which migration tools may strip out, so such properties should be identified, extracted, stored and preserved at an early stage of the preservation process. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-20]] ^s14
- Migration tools may introduce invisible changes to the content or the data, a risk reduced by devising acceptance criteria for what the transformed object must keep and confirming the outcome through quality assurance. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-22]] ^s15
- File format migration is not always the solution, and the aerospace industry has found the cost of migrating and validating older CAD files much higher than an emulation solution that keeps and maintains the original software. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-23]] ^s16
- Reducing the range of supported file formats reduces complexity and overheads, and a sound approach to preservation planning is to normalise rather than add multiple migration formats to a collection. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-28]] ^s17
- Consensus on a preservation format exists for some content types, such as WAV for audio archiving and TIFF for archiving image master files, the latter now being challenged by JPEG2000, while digital video lacks agreement and shows an uncontrolled proliferation of wrapper formats, delivery methods and encoding methods. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-30]] ^s18

## Terms

- **Proliferation**: the accumulation of many file formats and versions of formats in an organisation that does not normalise, making it hard to track which are at risk and which tools serve them. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-08]]
- **Significant properties**: on one view the essence of file content, the aspects of a format that carry the most meaning and value to the user and that a strategy may preserve in place of all aspects. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-19]]
- **Normalisation**: reducing the range of supported formats in a collection rather than adding further migration formats to it. [[10_markdown/documents/dpc-handbook-file-formats-and-standards#^dpc-28]]

## Open questions

- The chapter names documentation, adoption, licensing model, lossiness, metadata support and significant properties as factors without stating how they are weighed against each other in a concrete decision.
- Significant properties are presented as one view among possible ones, and the chapter does not say who decides which properties count as significant for a given collection.
- The recommendation to normalise and the observation that obsolescence is less severe than feared pull in different directions, and the chapter does not say how much normalisation the reduced risk still justifies.

## Appraisal

The Handbook is community reference literature rather than a policy, and its register is advisory throughout, which is both its limit and its use. It is the only source in this set that puts proliferation on a par with obsolescence, and that framing is the one that transfers to a vault, where the risk is not that Markdown becomes unreadable but that a project accumulates incompatible variants of its own conventions. The significant-properties passage is the conceptual counterpart to what a Markdown representation does, deciding in advance which aspects of a source have to survive conversion; the chapter treats that decision as open, which leaves the vault to make it explicitly. Its chronological anchoring is uneven, since the second-edition text keeps observations pegged to a decade before its own publication.

## Related

- [[20_distillates/documents/loc-recommended-formats-2025-2026]]
- [[20_distillates/documents/tna-selecting-file-formats-2008]]
