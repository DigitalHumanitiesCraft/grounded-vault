---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-critical-apparatus]]"
topics: ["[[Provenance]]", "[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: TEI P5, Critical Apparatus

The TEI critical apparatus chapter defines how a variant reading is bound to the witnesses attesting it and how an apparatus entry is addressed against the text it varies, which gives the vault a worked-out standard for reading-level attribution and for pointing at a location in a text.

## Core statements

- The TEI critical apparatus module allows variation to be encoded so that the compressed notes of a printed critical edition may be generated, and it also models the variation so that interactive editions in which readers choose which witness readings to display are possible. [[10_markdown/documents/tei-p5-critical-apparatus#^t01]] ^s1
- Information about variant readings may be recorded in a series of apparatus entries, each entry documenting one variation, or set of readings, in the text. [[10_markdown/documents/tei-p5-critical-apparatus#^t02]] ^s2
- The TEI makes no recommendations as to which text-critical methods are best suited to any given text. [[10_markdown/documents/tei-p5-critical-apparatus#^t03]] ^s3
- Editors wishing to distinguish witness readings from conjectures by modern editors may wish to use wit to indicate the former and source for the latter. [[10_markdown/documents/tei-p5-critical-apparatus#^t04]] ^s4
- Unlike choice, the app element allows the representation of many different versions of the same passage taken from different sources. [[10_markdown/documents/tei-p5-critical-apparatus#^t05]] ^s5
- The identification of discrete textual variations or apparatus entries is not a purely mechanical process, different editors will group readings differently, and no rules are given here as to how to collect readings into apparatus entries. [[10_markdown/documents/tei-p5-critical-apparatus#^t06]] ^s6
- The attributes loc, from and to are used to link the apparatus entry to the base text where one is present. [[10_markdown/documents/tei-p5-critical-apparatus#^t07]] ^s7
- The elements that should be used to tag individual readings within an apparatus entry are lem, which contains the lemma or base text of a textual variation, and rdg, which contains a single reading within a textual variation. [[10_markdown/documents/tei-p5-critical-apparatus#^t09]] ^s8
- In this chapter the term lemma is used in the text-critical sense of the reading accepted as that of the original or of the base text, which differs from the sense the word carries elsewhere in the Guidelines. [[10_markdown/documents/tei-p5-critical-apparatus#^t10]] ^s9
- In recording readings within an apparatus entry the rdg element should always be used, and each app usually contains at least one rdg, though it may contain only notes. [[10_markdown/documents/tei-p5-critical-apparatus#^t11]] ^s10
- The lem element may be used to record the base text of the source edition, to mark the readings of a base witness, to indicate the preference of an editor or encoder for a particular reading, or to indicate precisely to which portion of the main text the variation applies. [[10_markdown/documents/tei-p5-critical-apparatus#^t12]] ^s11
- The wit attribute of the class att.witnessed contains a space-delimited list of one or more pointers indicating the witnesses which attest to a given reading. [[10_markdown/documents/tei-p5-critical-apparatus#^t13]] ^s12
- The wit attribute is required if the apparatus gathers together readings from different witnesses, and may be omitted in an apparatus recording the readings of only one witness. [[10_markdown/documents/tei-p5-critical-apparatus#^t14]] ^s13
- The resp and cert attributes may be used to indicate the person responsible for the editorial decision being recorded and the degree of certainty associated with that decision by the person carrying out the encoding. [[10_markdown/documents/tei-p5-critical-apparatus#^t15]] ^s14
- Because the hand attribute indicates a particular manuscript hand it is intelligible only on a reading from a single witness, so an encoder wishing to indicate that a reading from a list in wit is in a particular hand should use the witDetail element. [[10_markdown/documents/tei-p5-critical-apparatus#^t16]] ^s15
- Broadly, the attribute wit identifies the physical entity in which the reading is found, hand refers to the agent responsible for inscribing that reading in that physical entity, and source indicates the scholar responsible for asserting the existence of that reading in that physical entity, though the categories may blur in some cases. [[10_markdown/documents/tei-p5-critical-apparatus#^t17]] ^s16
- A given reading is associated with the set of witnesses attesting it by listing the witnesses in the wit attribute on the rdg or lem element. [[10_markdown/documents/tei-p5-critical-apparatus#^t18]] ^s17
- The witDetail element is a specialized note which can be linked both to a reading and to one or more of the witnesses for that reading, the link to the reading being inferred from its position or made explicit by the target attribute and the link to the witness being made by the wit attribute. [[10_markdown/documents/tei-p5-critical-apparatus#^t19]] ^s18
- Without a target attribute a witDetail refers to the closest preceding lem or rdg, and target must be used if there is any ambiguity or if the witDetail refers to multiple readings. [[10_markdown/documents/tei-p5-critical-apparatus#^t20]] ^s19
- The wit element may be used to transcribe the exact form in which a source edition records the witnesses to a particular reading, retaining that form being particularly important in cases of ambiguity in the information or uncertainty as to the correct interpretation. [[10_markdown/documents/tei-p5-critical-apparatus#^t21]] ^s20
- Using the wit attribute, with witDetail where needed, is almost always to be preferred over the wit element, because the attribute is more succinct and makes the automated verification of correct witness references easier. [[10_markdown/documents/tei-p5-critical-apparatus#^t22]] ^s21
- A list of all identified witnesses should normally be supplied in the front matter of the edition or in the sourceDesc element of its header, either as a listBibl or as a listWit containing a series of witness elements. [[10_markdown/documents/tei-p5-critical-apparatus#^t23]] ^s22
- A unique siglum should always be supplied for a witness using the global xml:id attribute, and this identifier can then be used elsewhere to refer to that particular witness. [[10_markdown/documents/tei-p5-critical-apparatus#^t24]] ^s23
- The minimal information provided by a witness list is the set of sigla for all the witnesses named in the apparatus. [[10_markdown/documents/tei-p5-critical-apparatus#^t25]] ^s24
- The empty elements witStart, witEnd, lacunaStart and lacunaEnd may occur within any lem or rdg element and indicate the beginning or end of a fragmentary witness or of a lacuna within a witness. [[10_markdown/documents/tei-p5-critical-apparatus#^t26]] ^s25
- Three different methods may be used to link a critical apparatus to the text, the location-referenced method, the double-end-point-attached method and the parallel segmentation method. [[10_markdown/documents/tei-p5-critical-apparatus#^t27]] ^s26
- The location-referenced and the double end-point methods may be used with either in-line or external apparatus, while the parallel segmentation method may only be used for in-line apparatus. [[10_markdown/documents/tei-p5-critical-apparatus#^t28]] ^s27
- Any document containing app elements requires a variantEncoding declaration in the encodingDesc element of its TEI header, whose method attribute indicates the encoding method used and whose location attribute indicates whether the apparatus appears within the running text or external to it. [[10_markdown/documents/tei-p5-critical-apparatus#^t29]] ^s28
- In the location-referenced method the apparatus is linked to the base text by indicating explicitly only the block of text on which there is a variant, noted usually by a canonical reference scheme or by line number in the edition. [[10_markdown/documents/tei-p5-critical-apparatus#^t30]] ^s29
- When the apparatus is linked to the text by means of location references it is not possible to find automatically the precise portion of text varied by the readings. [[10_markdown/documents/tei-p5-critical-apparatus#^t31]] ^s30
- Where the apparatus is intended to be complete enough to allow the reconstruction of the witnesses, simple location-reference methods are unlikely to be as successful as the other two methods, which allow the unambiguous reconstruction of the lemma from the encoding. [[10_markdown/documents/tei-p5-critical-apparatus#^t32]] ^s31
- The double end-point attachment method explicitly indicates both the beginning and the end of the lemma in the base text and thereby permits unambiguous matching of each variant reading against its lemma. [[10_markdown/documents/tei-p5-critical-apparatus#^t33]] ^s32
- In the double end-point attachment method the from and to attributes of app carry identifiers which occur at the beginning and ending points of the reading in the base text, and where no other markup is present at those points they should be marked with the anchor element. [[10_markdown/documents/tei-p5-critical-apparatus#^t34]] ^s33
- Where an exhaustive list of witnesses is available, an application can determine which manuscripts witness the base reading by noting which witnesses are attested as having a variant reading and inferring the base text reading for all others, after adjusting for fragmentary witnesses and for witnesses carrying overlapping variant readings. [[10_markdown/documents/tei-p5-critical-apparatus#^t35]] ^s34
- The double end-point attachment method is designed to cope with overlapping lemmata, which the parallel segmentation method cannot handle and which it would require to be split into pieces. [[10_markdown/documents/tei-p5-critical-apparatus#^t36]] ^s35
- Because creation and interpretation of double end-point attachment apparatus are lengthy and difficult, such apparatus are likely to be created and examined by scholars usually only with mechanical assistance. [[10_markdown/documents/tei-p5-critical-apparatus#^t37]] ^s36
- In the parallel segmentation method all variants at any point of the text are expressed as variants on one another, no two variations can overlap although they may nest, and with a positive apparatus an application can straightforwardly extract the full text of any one witness from the apparatus. [[10_markdown/documents/tei-p5-critical-apparatus#^t38]] ^s37
- The parallel segmentation method is less convenient for textual traditions where establishing a base text with variations from it is not a satisfactory goal for the edition, or in some cases where every detail of variation needs to be modeled. [[10_markdown/documents/tei-p5-critical-apparatus#^t39]] ^s38
- In the parallel segmentation method each segment of text on which there is variation is marked by an app element, a preferred or base reading, where one exists, is tagged with lem, and each reading is given in a rdg element. [[10_markdown/documents/tei-p5-critical-apparatus#^t40]] ^s39
- The parallel segmentation method must be used in-line and cannot be used with external apparatus, and apparatus encoded with it may be translated into the double end-point attachment method and back without loss of information. [[10_markdown/documents/tei-p5-critical-apparatus#^t41]] ^s40
- Parallel segmentation cannot deal very gracefully with variants which overlap without nesting, and such variants must be broken up into pieces in order to keep all witnesses synchronized. [[10_markdown/documents/tei-p5-critical-apparatus#^t42]] ^s41
- An apparatus does not need to be given at the location in the transcription where the observation occurs and may instead be stored in a separate place in the same file or in another file and point to the location at which it is meant to be used. [[10_markdown/documents/tei-p5-critical-apparatus#^t43]] ^s42
- Where possible it is recommended that methods other than the location-referenced one use the from attribute to point to an xml:id attribute on an anchor or other element at the location where the apparatus observation takes place. [[10_markdown/documents/tei-p5-critical-apparatus#^t44]] ^s43
- The from attribute is of the datatype teidata.pointer and thus contains a URI as a value, so it can point directly to an xml:id, to an xml:id in another local file, or to a file identified by any URL or URN. [[10_markdown/documents/tei-p5-critical-apparatus#^t45]] ^s44
- URLs can contain XPointer schemes including xpath(), range() and string-range(), which can be used in providing the location of an app that is stored separately from the text to which it applies. [[10_markdown/documents/tei-p5-critical-apparatus#^t46]] ^s45
- Where only the from attribute is provided it supplies the location of the textual variance the apparatus documents, and where it contains an XPointer scheme identifying a range it records the starting and ending of that range as in the double end-point attachment method, so that a to attribute is unnecessary. [[10_markdown/documents/tei-p5-critical-apparatus#^t47]] ^s46
- Encoding variation at higher structural levels must not break TEI's Abstract Model, so it is an error to have a div in the lem but a p in a rdg inside the same apparatus entry, or to place a p inside another p or an l inside an l. [[10_markdown/documents/tei-p5-critical-apparatus#^t48]] ^s47
- An omission in one witness should be encoded using an empty rdg, and an interpolation that the editor does not wish to show in the base text using an empty lem. [[10_markdown/documents/tei-p5-critical-apparatus#^t49]] ^s48
- A transposition cannot be encoded with a single app, and the mutually exclusive apps are linked via the exclude attribute, while the copyOf attribute avoids repeating the transposed lines. [[10_markdown/documents/tei-p5-critical-apparatus#^t50]] ^s49
- Apparatus entries may nest when there is variation at both higher and lower structural levels. [[10_markdown/documents/tei-p5-critical-apparatus#^t51]] ^s50

## Terms

- **witness**: one of the different sources among which a scholarly edition records the known variations of a text; witnesses may include authorial or other manuscripts, printed editions of the work, early translations, or quotations of a work in other texts [[10_markdown/documents/tei-p5-critical-apparatus#^t01]]
- **apparatus entry**: one entry in a series recording variant readings, documenting one variation, or set of readings, in the text [[10_markdown/documents/tei-p5-critical-apparatus#^t02]]
- **positive apparatus**: an apparatus in which each reading records every attestation, as against a negative apparatus recording merely witnesses that deviate from the base text [[10_markdown/documents/tei-p5-critical-apparatus#^t03]]
- **lemma**: the reading accepted as that of the original or of the base text [[10_markdown/documents/tei-p5-critical-apparatus#^t10]]
- **siglum**: the unique identifier of a witness, supplied with the global xml:id attribute and used elsewhere to refer to that witness [[10_markdown/documents/tei-p5-critical-apparatus#^t24]]

## Open questions

- The chapter leaves the grouping of readings into apparatus entries to the editor and states no rules for it, so the represented text does not say what makes two variants one entry rather than two.
- The chapter recommends the wit attribute over the wit element because automated verification of witness references is easier with it, without saying what such verification checks or against which register of sigla it runs.
- The chapter treats the sigil as a pointer within the document or file set and does not address what happens to the binding of a reading to its witness when a witness is identified across documents or over time.

## Appraisal

The chapter is normative documentation of a maintained community standard rather than a research argument, so its statements carry the weight of an agreed encoding practice and not of an empirical finding. Its value for this vault lies in a worked-out separation the vault needs elsewhere, the distinction between the physical carrier of a statement, the agent who inscribed it, and the scholar who asserts that the carrier holds it. Its limits are that the standard governs a markup vocabulary and leaves the editorial decisions it depends on, above all the segmentation into apparatus entries, explicitly outside the encoding, so an apparatus records attribution without recording the judgment that produced it.

## Related

- [[30_assertions/MOC-Provenance]]
- [[30_assertions/MOC-Architecture]]
