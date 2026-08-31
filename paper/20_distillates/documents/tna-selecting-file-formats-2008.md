---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tna-selecting-file-formats-2008]]"
topics: ["[[Architecture]]", "[[Provenance]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: TNA Guidance Note 1, Selecting file formats for long-term preservation

The National Archives sets out twelve criteria for choosing a file format for long-term preservation and names the trade-offs those criteria create, among them the loss of structure and context that plain text imposes.

## Core statements

- The National Archives does not specify or require particular file formats for records to be transferred, and holds that the choice of format should be determined by the functional requirements of the record creation process. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-02]] ^s1
- Format selection should be determined not only by the immediate requirements of the situation but with long-term sustainability in mind, since an electronic record is not fully fit-for-purpose unless it is sustainable throughout its required life cycle. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-05]] ^s2
- Managing large collections of electronic records is greatly simplified by minimising the number of separate formats involved, and it is useful to identify a minimal set that meets both business needs and the sustainability criteria and to restrict data creation to that set. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-06]] ^s3
- Preserving the data elements of a word-processed document as plain ASCII text with the illustrations as separate image files results in a loss of structure, such as the formatting of the text, and of context, such as the internal pointers to the illustrations. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-08]] ^s4
- There is a conflict between formats that can be accessed and formats that can be re-used, which in some cases can only be reconciled by using different formats for preservation and for presentation. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-09]] ^s5
- The note names twelve criteria for format selection: ubiquity, support, disclosure, documentation quality, stability, ease of identification and validation, intellectual property rights, metadata support, complexity, interoperability, viability and re-usability. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-10]] ^s6
- Formats that are well established and in widespread use tend to have broader and longer-lasting support from software suppliers than niche formats, which makes popular formats preferable in many cases. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-11]] ^s7
- The availability of a wide range of supporting software tools removes dependence on any single supplier for access and is therefore preferable, although the ubiquity of a single tool may counterbalance this. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-12]] ^s8
- Formats whose technical specifications are available in the public domain are recommended and open standard formats are highly recommended wherever possible, while the advantages of some open formats may come at the cost of some loss in structure, context and functionality, as with ASCII, or of some reusability, as with PDF. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-13]] ^s9
- The availability of format documentation is not sufficient in itself; the documentation must be comprehensive, accurate and comprehensible enough to allow objects in the format to be interpreted by a human user or through newly developed access software. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-14]] ^s10
- A format specification should be stable and not subject to constant or major changes over time, and new versions of the format should be backwards compatible. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-15]] ^s11
- Accurately identifying the format of a file and confirming that the file is a valid example of that format is vital to continued use, and well-designed formats facilitate identification through magic numbers and version information inside the file structure. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-16]] ^s12
- Formats unencumbered by patents are recommended, because patents or other intellectual property constraints may limit the present or future use of objects in that format. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-17]] ^s13
- Metadata carried inside a file can provide information on both the provenance and the technical characteristics of the data. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-18]] ^s14
- In general, formats that offer metadata support are preferable to those that do not. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-19]] ^s15
- A format should support the full range of features required for its designated purpose while over-specified formats are to be avoided, since the more complex a format is, the more costly it will be to manage and preserve. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-20]] ^s16
- Formats supported by a wide range of software or independent of platform are most desirable for exchanging records, and this also tends to support long-term sustainability by facilitating migration from one technical environment to another. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-21]] ^s17
- Formats that provide error-detection facilities, such as a CRC value, are more robust and thus preferable. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-22]] ^s18
- Certain types of data must retain the ability to be processed if they are to have any re-use value, and converting a spreadsheet into PDF effectively removes much of its ability to be processed. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-23]] ^s19
- Under Metadata Support the note lists two factors, the degree of support provided by the software environment used to create the files and the extent to which externally stored metadata is used in its place. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-26]] ^s20

## Terms

- **Disclosure**: the criterion asking whether the technical specification of a format is available in the public domain, as it invariably is with open standards. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-13]]
- **Viability**: the criterion asking whether a format provides error-detection facilities allowing corruption to be detected. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-22]]
- **Re-usability**: the criterion asking whether data in the format retains the ability to be processed. [[10_markdown/documents/tna-selecting-file-formats-2008#^tna-23]]

## Open questions

- The twelve criteria are listed without weighting or a procedure for resolving conflicts between them, so the note does not say what to do when ubiquity and disclosure point at different formats.
- The note dates from 2008 and its examples are drawn from the format landscape of that time, and it does not state how the criteria are to be reapplied as that landscape changes.
- The trade-off between access and re-use is named but not resolved beyond the suggestion of keeping two formats, and the note leaves open how the relation between the two copies is to be recorded.

## Appraisal

The note is guidance from a national archive and states criteria rather than verdicts, which is why it stays usable eighteen years after publication while its examples have aged. Its value for this vault is that it separates two things a format decision usually conflates, the accessibility of a rendering and the processability of the content, and says plainly that the two may require different formats. The ASCII example is the sharpest counterweight in the source set to a plain-text architecture, because it names precisely what is lost, the structure of the text and the internal pointers between its parts. What the note leaves the reader is a list without weights, so it cannot decide a case on its own, only frame one.

## Related

- [[20_distillates/documents/loc-recommended-formats-2025-2026]]
- [[20_distillates/documents/dpc-handbook-file-formats-and-standards]]
