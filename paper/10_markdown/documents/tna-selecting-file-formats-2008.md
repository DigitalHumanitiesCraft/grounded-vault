---
type: representation
source-type: document
source: "[[00_sources/tna-selecting-file-formats.pdf]]"
converter: "MarkItDown; page furniture, running heads and PDF bullet artefacts removed by the agent, headings and lists restored"
channel: collection
metadata:
  title: "Digital Preservation Guidance Note 1: Selecting File Formats for Long-Term Preservation"
  creator: "Head of Digital Preservation Research, The National Archives (UK)"
  date: "2008-08"
  format: "pdf"
  identifier: "https://cdn.nationalarchives.gov.uk/documents/selecting-file-formats.pdf"
  license: "OGL-UK-3.0; Crown copyright, licensed under the Open Government Licence v3.0"
  confidential: false
  extent: "Partial. Contains section 1 Introduction, section 2 Selection issues with all twelve criteria 2.1 to 2.12, and section 4 Conclusion. Excluded are the cover, the document control block, the contents list and section 3 Evaluating formats: sources of information, which describes PRONOM lookup procedures rather than criteria."
created: 2026-08-10
updated: 2026-08-10
---

# Digital Preservation Guidance Note 1: Selecting file formats for long-term preservation

## 1 Introduction

This document is one of a series of guidance notes produced by The National Archives, giving general advice on issues relating to the preservation and management of electronic records. It is intended for use by anyone involved in the creation of electronic records that may need to be preserved over the long term, as well as by those responsible for preservation. ^tna-01

This guidance note provides information for the creators and managers of electronic records about file format selection. Please note that The National Archives does not specify or require the use of any particular file formats for records which are to be transferred. Choice of file format should always be determined by the functional requirements of the record creation process. Record creators should be aware however, that long-term sustainability will become a requirement, both for ongoing business purposes and archival preservation. Sustainability costs are inevitably minimised when this factor is taken into account prior to data creation. Failure to do so often makes later attempts to bring electronic records into a managed and sustainable regime an expensive, complex and, generally, less successful process. ^tna-02

This guidance note sets out a range of criteria the aim of which is to help data creators and archivists make informed choices about file format issues. ^tna-03

## 2 Selection issues

File formats encode information into forms that can only be processed and rendered comprehensible by very specific combinations of hardware and software. The accessibility of that information is therefore highly vulnerable in today's rapidly evolving technological environment. This issue is not solely the concern of digital archivists, but of all those responsible for managing and sustaining access to electronic records over even relatively short timescales. ^tna-04

The selection of file formats for creating electronic records should therefore be determined not only by the immediate and obvious requirements of the situation, but also with long-term sustainability in mind. An electronic record is not fully fit-for-purpose unless it is sustainable throughout its required life cycle. ^tna-05

The practicality of managing large collections of electronic records, whether in a business or archival context, is greatly simplified by minimising the number of separate file formats involved. It is useful to identify a minimal set of formats which meet both the active business needs and the sustainability criteria below, and restrict data creation to these formats. ^tna-06

This guidance note is primarily concerned with the selection of file formats for data creation, rather than the conversion of existing data into 'archival' formats. However, the criteria described are equally applicable to the latter. ^tna-07

Selecting file formats for migration introduces some additional issues. Formats for migration must meet the requirements for both preservation of authenticity and ease of access. For example, the data elements of a word-processed document could be preserved as plain ASCII text, together with any illustrations as separate image files. However, this would result in a loss of structure (e.g. the formatting of the text), and of some context (e.g. the internal pointers to the illustrations). ^tna-08

There is also a subtly different conflict between the need for data formats that can be accessed and those that can be re-used. From a preservation and re-use perspective, data must be maintained in a form that can be processed. For the purposes of access, however, control of the formatting may well be the most important criteria, and in some cases it may be desirable for the data not to be able to be processed by end users. In some cases it may only be possible to reconcile these differences by using different formats for preservation and presentation purposes. ^tna-09

The following criteria should be considered by data creators when selecting file formats:

- Ubiquity
- Support
- Disclosure
- Documentation quality
- Stability
- Ease of identification and validation
- Intellectual Property Rights
- Metadata Support
- Complexity
- Interoperability
- Viability
- Re-usability
^tna-10

These criteria are elaborated in the following sections:

### 2.1 Ubiquity

The laws of supply and demand dictate that formats which are well established and in widespread use will tend to have broader and longer-lasting support from software suppliers than those that have a niche market. There is also likely to be more comprehensive community support amongst users. Popular formats are therefore preferable in many cases. ^tna-11

### 2.2 Support

The extent of current software support is a major factor for consideration. The availability of a wide range of supporting software tools removes dependence on any single supplier for access, and is therefore preferable. In some cases however, this may be counterbalanced by the ubiquity of a single software tool. ^tna-12

### 2.3 Disclosure

Those responsible for the management and long-term preservation of electronic records require access to detailed technical information about the file formats used. Formats that have technical specifications available in the public domain are recommended. This is invariably the case with open standards, such as JPEG. The developers of proprietary formats may also publish their specifications, either freely (for example, PDF), or commercially (as is the case with the Adobe Photoshop format specification, which is included as part of the Photoshop Software Development Kit). The advantages of some open formats may come at the cost of some loss in structure, context, and functionality (e.g. ASCII), or the preservation of formatting at the cost some reusability (e.g. PDF). Proprietary formats frequently support features of their creating software, which open formats do not. The tension between these needs is sometimes unavoidable, although the range and sophistication of open formats is increasing all the time. The use of open standard formats is however highly recommended wherever possible. ^tna-13

### 2.4 Documentation quality

The availability of format documentation is not, in itself, sufficient; documentation must also be comprehensive, accurate and comprehensible. Specifically, it should be of sufficient quality to allow interpretation of objects in the format, either by a human user or through the development of new access software. ^tna-14

### 2.5 Stability

The format specification should be stable and not subject to constant or major changes over time. New versions of the format should also be backwards compatible. ^tna-15

### 2.6 Ease of identification and validation

The ability to accurately identify the format of a data file and confirm that it is a valid example of that format, is vital to continued use. Well-designed formats facilitate identification through the use of 'magic numbers' and version information within the file structure. The availability of tools to validate the format is also a consideration. ^tna-16

### 2.7 Intellectual Property Rights

Formats may utilise technologies encumbered by patents or other intellectual property constraints, such as image compression algorithms. This may limit present or future use of objects in that format. In particular, 'submarine patents' (when previously undisclosed patent claims emerge), can be a concern. Formats that are unencumbered by patents are recommended. ^tna-17

### 2.8 Metadata Support

Some file formats make provision for the inclusion of metadata. This metadata may be generated automatically by the creating application, entered by the user, or a combination of both. This metadata can have enormous value both during the active use of the data and for long-term preservation, where it can provide information on both the provenance and technical characteristics of the data. For example, a TIFF file may include metadata fields to record details such as the make and model of scanner, the software and operating system used, the name of the creator, and a description of the image. Similarly, Microsoft Word documents can include a range of metadata to support document workflow and version control, within the document properties. The value of such metadata will depend upon: ^tna-18

- The degree of support provided by the software environment used to create the files,
- The extent to which externally stored metadata is used in its place. (For example if records are stored within an Electronic Records Management System).
^tna-26

In general, formats that offer metadata support are preferable to those that do not. ^tna-19

### 2.9 Complexity

Formats should be selected for use on the basis that they support the full range of features and functionality required for their designated purpose. It is equally important, however to avoid choosing over-specified formats. Generally speaking the more complex the format, the more costly it will be to both manage and preserve. ^tna-20

### 2.10 Interoperability

The ability to exchange electronic records with other users and IT systems is also an important consideration. Formats that are supported by a wide range of software or are platform-independent are most desirable. This also tends to support long-term sustainability of data by facilitating migration from one technical environment to another. ^tna-21

### 2.11 Viability

Some formats provide error-detection facilities, to allow detection of file corruption that may have occurred during transmission. Many formats include a CRC (Cyclic Redundancy Check) value for this purpose, but more sophisticated techniques are also used. For example, the PNG format incorporates byte sequences to check for three specific types of error that could be introduced. Formats that provide facilities such as these are more robust, and thus preferable. ^tna-22

### 2.12 Re-usability

Certain types of data must retain the ability to be processed if they are to have any re-use value. For example, conversion of a spreadsheet into PDF format effectively removes much of its ability to be processed. The requirement to maintain a version of the record that can be processed must also be considered. ^tna-23

## 4 Conclusion

There are many issues to be considered when selecting file formats extending beyond the immediate and obvious requirements of the situation. It may not be possible to select formats that meet all criteria in every case; however, new formats and revisions of existing formats are constantly being developed. This guidance note should assist data creators to make informed decisions about file format selection from the ever-changing choices available. ^tna-24

The adoption of sustainable file formats for electronic records brings benefits to data creators, data managers and digital archivists. Selection decisions informed by the criteria described above will greatly enhance the sustainability of the records created. ^tna-25
