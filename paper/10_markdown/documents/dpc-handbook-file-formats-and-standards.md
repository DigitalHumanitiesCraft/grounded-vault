---
type: representation
source-type: document
source: "[[00_sources/dpc-handbook-file-formats-and-standards.html]]"
converter: "agent; the saved HTML page stripped of navigation, share widgets and page furniture, headings and lists carried over unchanged"
channel: collection
metadata:
  title: "File formats and standards (Digital Preservation Handbook, 2nd Edition, Technical solutions and tools)"
  creator: "Digital Preservation Coalition, Glasgow"
  date: "2015"
  format: "html"
  identifier: "https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards"
  license: "OGL-UK-3.0; Handbook text licensed under the Open Government Licence v3.0, attribution required"
  confidential: false
  extent: "Partial. Contains the chapter from its Introduction through its Conclusion. Excluded are the illustration credit line, the Resources link list and the pointer to the case studies section."
created: 2026-08-10
updated: 2026-08-10
---

# File formats and standards

## Introduction

The management of file formats should be considered in the wider strategic context of preservation planning. What can your organisation afford to do? How much developer effort will it require? What do the users require from your collections? Are you committing yourself to a storage problem? At all times, the answer to digital preservation issues is not to try and "do everything". Your strategy ought to move you towards simple and practical actions, rather than trying to support more file formats than you need. ^dpc-01

The purpose of this section is not to provide a detailed or exhaustive list of current formats for different types of content but to draw attention to the broader implications of file formats for their application, and implications for preservation. ^dpc-02

A substantial part of this chapter refers to the possible selection of a file format for migration purposes. While migration is a valid preservation strategy, and quite common for many file formats, it is not the only approach or solution. Where appropriate, the chapter will refer to other suitable methods for preservation. ^dpc-03

## File formats organised by content types

Different content types have, over time, developed their own file formats as they strive to accommodate functionality specific to their needs. The main content types are images, video, audio and text; however, a growing number of formats are being structured to address the demands of new media, including formats for 3D models and archiving the web. ^dpc-04

File formats vary enormously in terms of complexity, with some data being encoded in many layers. In some cases the file formats involved are just one part of a larger picture, a picture that includes software, hardware, and even entire information environments. ^dpc-05

For further advice on preservation of specific types of digital content and associated file formats see the Content-specific preservation case studies in the Handbook.

## File formats - what should we be worrying about?

### Obsolescence

Formats evolve as users and developers identify and incorporate new functionality. New formats, or versions of formats, may introduce file format obsolescence as newer generations of software phase out support for older formats. When software does not provide for backwards compatibility with older file formats, data may become unusable. Both open source and commercial formats are vulnerable to obsolescence: vendors sometimes use planned obsolescence to entice customers to upgrade to new products while open source software communities may withdraw support for older formats if these are no longer generally needed by the community. Obsolescence can also be accidental: both businesses and open source communities can fail. ^dpc-06

File format format obsolescence is a risk that needs to be understood. That said, the problem may not be as severe as the digital preservation community perceived it to be some 10 years ago. Many established file formats are still with us, still supported, and still usable. It is quite likely that the majority of file formats you deal with will be commonly understood and well supported. ^dpc-07

### Proliferation

Arguably, in some sectors, proliferation is more of a challenge than obsolescence. If formats aren't normalised then an organisation can end up with a large number of different file formats, and versions of those formats: e.g. lots of different versions of PDF, word, image formats etc. In domains which develop rapidly evolving bespoke data formats this problem can be exacerbated. Tracking and managing all these formats - which ones are at risk, and which tools can be used for each one - can be a serious challenge. ^dpc-08

Your digital preservation strategy should strive to mitigate the effects of obsolescence and proliferation. Strategies as migration, emulation, normalisation and a careful selection of file formats are all valid and worth considering, in the context of your collections and your organisation. ^dpc-09

## Aspects of file formats for digital preservation

### Selecting target formats for preservation

Not all digital formats are suited or indeed designed for archiving or preservation. Any preservation policy should therefore recognise the requirements of the collection content and decide upon a file format which best preserves those qualities. Pairing content with a suitable choice of preservation format or access format; identifying what is important in the content. ^dpc-10

Below we suggest some factors to consider in selecting your preferred file formats:

### Open source vs proprietary?

Open source formats, such as JPEG2000, are very popular due to their non-proprietary nature and the sense of ownership that stakeholders can attain with their use. However, the choice of open source versus proprietary formats is not that simple and needs to be looked at closely. Proprietary formats, such as TIFF, are seen as being very robust; however, these formats will ultimately be susceptible to upgrade issues and obsolescence if the owner goes out of business or develops a new alternative. Similarly, open source formats can be seen as technologically neutral, being non-reliant on business models for their development however they can also been seen as vulnerable to the susceptibilities of the communities that support them. ^dpc-11

Although such non-proprietary formats can be selected for many resource types this is not universally the case. For many new areas and applications, e.g. Geographical Information Systems or Virtual Reality only proprietary formats are available. In such cases a crucial factor will be the export formats supported to allow data to be moved out of (or into) these proprietary environments. ^dpc-12

### Documentation and standards

The availability of documentation - for example, published specifications - is an important factor in selecting a file format. Documentation may exist in the form of vendor's specifications, an international standard, or may be created and maintained within the context of a user community. Look for a standard which is well-documented and widely implemented. Make sure the standard is listed in the PRONOM file format registry. ^dpc-13

### Adoption

A file format which is relied upon by a large user group creates many more options for its users. It is worth bearing in mind levels of use and support for formats in the wider world, but also finding out what organisations similar to you are doing and sharing best practice in the selection of formats. Wide adoption of a format can give you more confidence in your preservation strategy. ^dpc-14

### Lossless vs lossy

Lossy formats are those where data is compressed, or thrown away, as part of the encoding. The MP3 format is widely used for commercial distribution of music files over the web, because the lossy encoding process results in smaller file sizes. ^dpc-15

TIFF is one example of an image format that is capable of supporting lossless data. It could hold a high-resolution image. JPEG is an example of a lossy image file format. Its versatility, and small file size, makes it a suitable choice for creating an access copy of an image of smaller size for transmission over a network. It would not be appropriate to store the JPEG image as both the access and archival format because of the irretrievable data loss this would involve. ^dpc-16

One rule of thumb could be to choose lossless formats for the creation and storage of "archival masters"; lossy formats should only be used for delivery / access purposes, and not considered to be archival. A rule like this is particularly suitable for a digitisation project, particularly still images. ^dpc-17

### Support for metadata

Some file formats have support for metadata. This means that some metadata can be inscribed directly into an instance of a file (for example, JPEG2000 supports some rights metadata fields). This can be a consideration, depending on your approach to metadata management. ^dpc-18

### Significant properties of file formats

This is a complex area. One view regards significant properties as the "essence" of file content; a strategy that gets to the heart of "what to preserve". What does the user community expect from the rendition? What aspects of the original are you trying to preserve? This strategy could mean you don't have to commit to preserving all aspects of a file format, only those that have the most meaning and value to the user. ^dpc-19

Significant properties may also refer to a very specific range of technical metadata that is required to be present in order for a file to be rendered (e.g. image width). Some migration tools may strip out this metadata, or it may become lost through other curation actions in the repository. The preservation strategy needs to prevent this loss happening. It thus becomes important to identify, extract, store and preserve significant properties at early stage of the preservation process. ^dpc-20

## Things we can do

There are many things you could do to support file formats in your digital archive, and there are many tools available to help you with these tasks. There are now so many that digital preservation tool registries are being developed to help you locate and assess them (see the Tools and the Resources sections)

### Tools for migration

Broadly, these are tools that transform a file format from an obsolete format into a newer format which can be supported. Many tools exist for doing this migration. They tend to confine themselves to doing one thing (e.g. ImageMagick only works for digital image objects). ^dpc-21

A migration tool is just one part of a migration pathway. The pathway must include a destination / target format, which you will have selected in line with guidance as suggested above.

Migration tools may introduce risks. One of these risks is "invisible" changes happening to the content or to the data in the migration. To reduce this risk, one strategy is to devise a set of acceptance criteria for what the transformed object must keep, e.g. in terms of formatting, look and feel, or even functionality, and confirm desired outcomes with a process of quality assurance. ^dpc-22

File format migration is not always the solution. Some CAD and CAM file formats cannot easily be migrated, for example. The aerospace industry has found that migration of older CAD files to a newer format requires a lot of validation, mainly because they are required by a regulatory framework to demonstrate that their data is sound and meets very strict standards. In short, the cost of migration and validation is (for them) much higher than an emulation solution, an approach which (in this case) involves keeping the CAD software and maintaining it. ^dpc-23

See also the Tools and Content-specific preservation sections.

### Tools for rendition

Broadly, these are tools that can read and play back a file format, so that the user community can read and interpret the resource; it's most commonly applied to files stored in accessible formats. A basic rendition tool would be PDF Reader. A more sophisticated rendition tool would be the Wellcome Library media player, which supports OCR texts, images, and audio-visual files. ^dpc-24

### Tools for file format identification

Tools that can identify aspects of file formats which are not immediately obvious from their file extension. They do this by reading the file format header, and thus can identify e.g. mimetype, size, version. Examples of such tools include PRONOM, JHOVE, and the NZ Metadata Extraction Tool (see Resources below). ^dpc-25

These tools are usefully deployed at point of ingest, so that you know from the start what sort of file formats you are taking into the archive.

Some identification tools can also point to likely rendition tools, or even (like PRONOM) suggest a migration path based on file format identification.

### Tools for file format validation

JHOVE is one of the few tools that is able to validate a file format. It does this by comparing an instance of a file format with sets of expected behaviours, which it stores in its library. JHOVE can report on certain file formats and tell whether they are valid and well-formed. ^dpc-26

### Collection surveys

Survey file formats in use / know what you have / characterisation of your collections. This again ties into a planning strategy, letting you know what you need to support, and the likely effort required to do this.

A survey should pay particular attention to versions of file formats, and software needed for their reading / rendition. If possible, gather any information about published specifications for these formats; some specs are published on the web. ^dpc-27

Useful emerging work in this area has taken place at the British Library, with projects on Sustainability Assessments and Collection Profiling. At time of writing there are no active links to these projects, but it is anticipated that the Sustainability Assessment work will be published on the DPC wiki. These are useful approaches and can be regarded as examples of current best practice. Even if you don't assess or profile to the same depth as the BL, the exercise is a practical and applicable one.

### Avoid Proliferation of File Types

Where possible, reduce the range of file formats you support, in order to reduce complexity. A sound approach to preservation planning is to normalise, rather than add multiple migration formats to your collection. The smaller the range of formats, the lower the overheads. ^dpc-28

### Community

Identify a consensus of agreement on target file formats; collaborate with institutions who hold similar collections to yours. What formats do they choose to work with? ^dpc-29

## Conclusion

For some kinds of content, there is consensus around the choice of preservation format. For example audio archiving where WAV is commonly used. In other areas consensus is much more difficult to achieve. The preservation of digital video is a complex area where progress has been stymied by a lack of agreement, and an uncontrolled proliferation of wrapper formats, delivery methods, and encoding methods. The choice of image file formats is slightly clearer, with a limited choice of formats for archiving and others for delivery. It has been generally agreed that the TIFF format is the correct format for archiving master files (the RAW or DNG format is also considered appropriate for archiving) but this is now being challenged by the JPEG2000 format which provides a far greater level of lossless compression compared to TIFF and is open source. ^dpc-30
