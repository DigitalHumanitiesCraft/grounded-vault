---
type: representation
source-type: document
source: "[[00_sources/loc-rfs-2025-2026.pdf]]"
converter: "MarkItDown; the two-column preference tables restructured by the agent into nested lists whose first level names the Preferred and Acceptable column, checked against the parallel HTML edition at loc.gov/preservation/resources/rfs/"
channel: collection
metadata:
  title: "Library of Congress Recommended Formats Statement 2025-2026"
  creator: "Library of Congress, Washington, D.C."
  date: "2025"
  format: "pdf"
  identifier: "https://www.loc.gov/preservation/resources/rfs/"
  license: "Public domain; work of the U.S. Government under 17 U.S.C. §105"
  confidential: false
  extent: "Partial. Contains the Introduction to the 2025-2026 revision without its Content Category Changes subsection, and section I. Textual Works, subsections ii (Digital) and iii (Electronic serials). Excluded are the table of contents, subsection i (Textual Works - Print) and the content areas II to XI."
created: 2026-08-10
updated: 2026-08-10
---

# Library of Congress Recommended Formats Statement 2025-2026

## Introduction to the 2025-2026 revision

The Recommended Formats Statement (RFS) is well into its second decade, having first launched in 2014. It remains an important tool for both the Library of Congress but also the wider community who seek to create, collect and preserve published works in all forms. The resource has evolved over its lifespan to reflect not only changing priorities and capabilities but also its impact on the cultural landscape. ^loc-01

### Digital Accessibility as an Evaluation Criterion

Since 2024, the RFS incorporates a preferred or acceptable format's potential to support digital accessibility as an evaluation criterion. These features include: ^loc-02

- Does this format support digital accessibility features such as those described in the W3C Accessibility Principles? For example,
  - Text alternatives for non-text content (such as alt text)
  - Captions and other alternatives for multimedia (and subtitles)
  - Can text content be structured (as in XML) or tagged (as in PDF) for screen readers?
  - Are dataset formats well-structured with page regions and headings identified, permitting tagged or marked up content, tables that are navigable to a screen reader and forms that can validate entries?
- In what way are accessibility features implemented in the format? Such as:
  - Are there specific metadata tags to indicate accessibility features such as alt text, captions, transcripts and the like?
  - Are embedded closed captions supported? Does the file rely on external data, such as WebVTT file for caption data?
^loc-03

Full details about the information gathering and reporting are available on Documenting Accessibility Features on the Sustainability of Digital Formats. Each format listed in the RFS has a corresponding entry on this resource with supporting in depth research. ^loc-04

It's important to note that the RFS does not require these accessibility features to be enabled for a format for inclusion in LC collections. However, but it is still important to understand the capacity for the format to support these features as user expectations and communities change and grow. ^loc-05

### Preferred and Acceptable Formats

The key underpinning to the RFS remains a focus on both global/community criteria and local/institutional criteria as key to preservation and long-term access. The global/community criteria have been based on the seven sustainability factors developed for the Library's Sustainability of Digital Formats website: Disclosure, Adoption, Transparency, Self-documentation (including accessibility support), External dependencies, Impact of patents and Technical protection mechanisms. Each of these factors may have different emphasis or importance depending on the community of practice and content type. Some may not be applicable or essential for every format. The local/institutional factors estimate the level of resources at The Library of Congress available to preserve and manage the content over time. These include Staff experience and expertise, Software/Hardware/Operating System availability, Representation/extent in LC collections/storage, Established workflow/functionality and Access options including support on the Library's website, loc.gov. The outcome of this analytical structure are clearer definitions of 'Preferred' and 'Acceptable' when categorizing digital file formats in the RFS. ^loc-06

The updated evaluation matrix with sample data is available for download.

- Preferred formats:
  - A. Global/community: Meets or exceeds benchmarks for all relevant sustainability factors
  - B. Local/institutional: The Library of Congress has the skills, experience, workflows, tools and systems to manage and preserve these formats in current systems with confidence.
^loc-07

- Acceptable formats:
  - A. Global/community: Meets minimum acceptability across benchmarks or does not meet all relevant sustainability factors.
  - B. Local/institutional: The Library of Congress can manage this format at a basic level of acquisition, management and preservation; and a greater ability for management and preservation is within the Library's capacity with further investment.
^loc-08

The success in using this model opens the possibility of adapting it to apply to those other characteristics of creative works, both physical and digital, which the RFS covers in its remit to address all types of creative works. ^loc-09

The Recommended Formats Statement is not intended to serve as an answer to all the questions raised in preserving and providing long-term access to creative content. For example, it does not provide instructions for receiving material into repositories, managing that content or undertaking the many ongoing tasks which will be necessary to maintain this content so that it may be used well into the future. Tackling each of those aspects is a project in and of itself as each form of content has a unique set of facets and nuances. The RFS provides guidance on identifying sets of formats which are not drawn so narrowly as to discourage creators from working within them, but will instead encourage creators to use them to produce works in formats which will make preserving them and making them accessible simpler. See the FAQ page for additional context. The Library hopes that the RFS will help make it realistic to build, grow and save creative output for our individual and collective benefit for generations to come. ^loc-10

### Conclusion

The Library of Congress, realizing its unique position, is pleased to be able to contribute a resource like the Recommended Formats Statement for the benefit of all involved with creative works. The commitment of time and resources to the ongoing revision and indeed improvement of the RFS reflects the priority the Library places on working collaboratively to ensure that all might succeed in our common goal to share and disseminate creative output and to benefit the nation and the world at large. Comments are always welcome through rfs@loc.gov. ^loc-11

## I. Textual Works

NOTE: See also Musical Scores

### ii. Textual Works – Digital

#### A. Technical Characteristics, in order of preference

- Preferred. Character encoding, in descending order of preference:
  1. UTF-8, UTF-16 (with BOM), US-ASCII
  2. ISO 8859
- Acceptable. Other character encodings not listed in Preferred section
^loc-12

#### B. Formats

- Preferred, as received:
  - XML-based markup formats, with included or accessible DTD/schema, XSD/XSL presentation stylesheet(s), and explicitly stated character encoding
  - EPUB3-compliant. (Other versions of EPUB are also preferred formats but EPUB3 is the most common.)
  - Other widely-used book DTDs/schemas (e.g., TEI, DocBook, etc.)
  - Page-layout formats
    - PDF/UA (ISO 14289-1-compliant)
    - PDF/A (ISO 19005-compliant)
    - PDF (highest quality available, with features such as searchable text, embedded fonts, lossless compression, high resolution images, device-independent specification of colorspace, content tagging; includes document formats such as PDF/X)
^loc-13

- Acceptable. Other structured or markup formats in order of preference:
  1. XHTML or HTML, with DOCTYPE declaration and presentation stylesheet(s)
  2. XML-based document formats (widely-used and publicly-documented), with presentation stylesheet(s) if applicable. Includes DOCX/OOXML 2012 (ISO 29500), ODF (ISO/IEC 26300) and OOXML (ISO/IEC 29500).
  3. SGML, with included or accessible DTD
  4. BITS (Book Interchange Tag Suite) version 2.0
  5. Page-layout formats
     - a. PDF (web-optimized)
  6. Other formats
     - a. Rich text format (RTF)
     - b. Plain text
     - c. Widely-used proprietary word-processing formats
^loc-14

#### C. Rarity and Special Features

- Preferred:
  - Limited editions (including those with special features such as high resolution images).
  - Editions with the greatest number of unique features (such as additional content, multimedia, interactive elements, etc.)
- Acceptable. Editions without these features
^loc-15

#### D. Completeness

- Preferred:
  - Complete work. For items published in a finite number of separate components, all elements published as part of the work and offered for sale or distribution must be submitted. Includes all associated external files and fonts considered integral to the publication.
  - All updates, supplements, releases, and supersessions published as part of the work and offered for sale or distribution must be submitted and received in a regular and timely manner for proper maintenance of the deposit.
^loc-16

#### E. Metadata

- Preferred:
  1. As supported by format (e.g., standards-based formats such as ONIX for Books, XMP, MODS, METS, or MARCXML either embedded in or accompanying the digital item):
     - a. Title
     - b. Creator
     - c. Publication/Creation Date or Start Date/End Date
     - d. Place of publication
     - e. Publisher/ producer/ distributor
     - f. ISBN/ISSN
     - g. Contact information
  2. If available:
     - a. Language of work
     - b. Other relevant identifiers (e.g., DOI, LCCN, original URL, etc.)
     - c. Edition
     - d. Subject descriptors
     - e. Abstracts
^loc-17

- Acceptable:
  1. As displayed on item:
     - a. Title
     - b. Creator
     - c. Publication/Creation Date or Start Date/End Date
     - d. Place of Publication
     - e. Publisher/Producer/Distributor
^loc-18

#### F. Technological Measures

Files must contain no measures (such as digital rights management technologies or encryption) that control access to or prevent use of the digital work. ^loc-19

### iii. Textual Works – Electronic serials

#### A. Technical Characteristics, in order of preference

- Preferred. Character encoding, in descending order of preference:
  1. UTF-8, UTF-16 (with BOM), US-ASCII
  2. ISO 8859
- Acceptable. Other character encodings not listed in Preferred section
^loc-20

#### B. Formats

- Preferred, as received:
  - Content compliant with the NISO JATS: Journal Article Tag Suite (ANSI/NISO Z39.96-2015) with XSD/XSL presentation stylesheet(s) and explicitly stated character encoding
  - Page-layout formats
    - PDF/UA (ISO 14289-1-compliant)
    - PDF/A (ISO 19005-compliant)
    - PDF (highest quality available, with features such as searchable text, embedded fonts, lossless compression, high resolution images, device-independent specification of colorspace; content tagging; includes document formats such as PDF/X)
^loc-21

- Acceptable. Other structured or markup formats in order of preference:
  1. Widely-used serials or journal non-proprietary XML-based DTDs/schemas with included or accessible DTD/schema, presentation stylesheet(s) and explicitly stated character encoding.
  2. Proprietary XML-based format for serials or journals (with documentation) with DTD/schema and presentation stylesheet(s)
  3. XHTML or HTML, with DOCTYPE declaration and presentation stylesheet(s)
  4. XML-based document formats (widely used and publicly documented). With presentation stylesheets, if applicable. Includes DOCX/OOXML 2012 (ISO 29500), ODF (ISO/IEC 26300) and OOXML (ISO/IEC 29500).
  5. Page-layout formats
     - a. PDF (web-optimized with searchable text)
  6. Other formats
     - a. Rich text format
     - b. Plain text
     - c. Widely used proprietary word processing or page-layout formats
     - d. Other text- or graphic-based formats not listed here that represent textual works
^loc-22

#### C. Rarity and Special Features

- Preferred:
  - Limited editions (including those with special features such as high resolution images)
  - Editions with the greatest number of unique features (such as additional content, multimedia, interactive elements, etc.)
- Acceptable. Editions without these features
^loc-23

#### D. Completeness

- Preferred:
  - Complete work. All elements considered integral to the publication and offered for sale or distribution must be submitted – e.g., articles, table(s) of contents, front matter, back matter, etc. Includes all associated external files and fonts considered integral to the publication.
  - All updates, supplements, releases, and supersessions published as part of the work and offered for sale or distribution must be submitted and received in a regular and timely manner for proper maintenance of the deposit.
- Acceptable. Editions without these features
^loc-24

#### E. Metadata

- Preferred:
  1. Title-level metadata (e.g., standards-based formats such as ONIX for Books, XMP, MODS, METS, or MARCXML either embedded in or accompanying the digital item):
     - a. Serial or journal title
     - b. ISSN and ISSN-L
     - c. Publisher
     - d. Frequency
     - e. Place of publication
  2. Structured metadata as relevant or applicable (e.g., standards-based formats such as ONIX for Books, XMP, MODS, METS, or MARCXML either embedded in or accompanying the digital item):
     - a. Volume(s)
     - b. Number(s)
     - c. Issue date(s)
     - d. Article title(s)
     - e. Article author(s)
     - f. Article identifier (DOI, original URL, etc.)
  3. Include if available:
     - a. Other descriptive metadata (e.g., subject heading(s), descriptor(s), abstract(s))
^loc-25

#### F. Technological Measures

Files must contain no measures (such as digital rights management technologies or encryption) that control access to or prevent use of the digital work. ^loc-26
