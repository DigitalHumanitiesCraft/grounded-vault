---
type: representation
source-type: document
source: "[[00_sources/tei-p5-tc-critical-apparatus.html]]"
converter: "MarkItDown 0.1.6 (HTML to Markdown), then agent-side reduction to the conceptually load-bearing sections"
channel: collection
metadata:
  title: "13 Critical Apparatus, in TEI P5: Guidelines for Electronic Text Encoding and Interchange, version 4.12.0"
  creator: "TEI Consortium"
  date: "2026-07-28"
  format: "html"
  identifier: "https://tei-c.org/release/doc/tei-p5-doc/en/html/TC.html"
  license: "CC-BY-3.0 OR BSD-2-Clause"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# 13 Critical Apparatus

Scope of this representation: the conceptually load-bearing prose of the chapter, meaning the apparatus model of the introduction and of section 13.1, the binding of a reading to its witnesses in 13.1.2 and 13.1.4, the fragmentary-witness mechanism in 13.1.5, the three linking methods and the other linking methods in 13.2, and the encoding strategies in 13.4. Left out are the full element and attribute specification tables, the XML examples, the transcription section 13.3, and the module summary 13.5. Inline cross-reference links of the source were flattened to their link text, and line breaks were rewrapped; the wording is otherwise that of the source. The source page numbers this chapter 13; earlier printed and cited states of the Guidelines number the same chapter 12, and the URL slug `TC.html` is stable across both.

## Introduction

Scholarly editions of texts, especially texts of great antiquity or importance, often record some or all of the known variations among different witnesses to the text. Witnesses to a text may include authorial or other manuscripts, printed editions of the work, early translations, or quotations of a work in other texts. Information concerning variant readings of a text may be accumulated in highly structured form in a critical apparatus of variants. This chapter defines a module for use in encoding such an apparatus of variants, which may be used in conjunction with any of the modules defined in these Guidelines. It also defines an element class which provides extra attributes for some elements of the core tag set when this module is selected. In printed critical editions, the apparatus takes the form of highly-compressed notes at the bottom of each page. TEI's critical apparatus module allows variation to be encoded so that such notes may be generated, but it also models the variation so that, for example, interactive editions in which readers can choose which witness readings to display are possible. ^t01

Information about variant readings (whether or not represented by a critical apparatus in the source text) may be recorded in a series of apparatus entries, each entry documenting one variation, or set of readings, in the text. ^t02

Scholarly practice in representing critical editions differs widely across disciplines, time periods, and languages. The TEI does not make any recommendations as to which text-critical methods are best suited to any given text. Editors will wish to consider questions such as: what source documents will be used; whether there will be a single base text or separately transcribed witnesses; whether each reading in an apparatus entry will record every attestation (a positive apparatus) or merely witnesses that deviate from the base text (a negative apparatus); whether the readings of most or all witnesses will be represented, or only a selection the editor deems relevant; what level of variation will require distinguishing one witness reading from another; whether conjectures (variant readings suggested by an editor) will be treated differently than readings found in witnesses; and whether there will be a need to distinguish different types of variation. ^t03

Different editorial methodologies will produce different answers to these questions, and those answers may influence choices of markup used in the edition. Editors wishing to distinguish witness readings from conjectures by modern editors may wish to use wit to indicate the former and source for the latter. Differences in types of variation might be marked using type or ana on the rdg element. ^t04

## 13.1 The Apparatus Entry, Readings, and Witnesses

The app element is in one sense a more sophisticated and complex version of the choice element introduced in 3.5.1 Apparent Errors as a way of marking points where the encoding of a passage in a single source may be carried out in more than one way. Unlike choice, however, the app element allows for the representation of many different versions of the same passage taken from different sources. ^t05

### 13.1.1 The Apparatus Entry

Individual textual variations are encoded using the app element, which groups together all the readings constituting the variation. The identification of discrete textual variations or apparatus entries is not a purely mechanical process; different editors will group readings differently. No rules are given here as to how to collect readings into apparatus entries. ^t06

The attributes loc, from, and to, are used to link the apparatus entry to the base text, if present. In such cases, several methods may be used for such linkage, each involving a slightly different usage for these attributes. ^t07

Each app element usually comprises one or more readings, which in turn are encoded using the rdg or other elements. ^t08

### 13.1.2 Readings

Individual readings are the crucial elements in any critical apparatus of variants. The following elements should be used to tag individual readings within an apparatus entry: lem (lemma) contains the lemma, or base text, of a textual variation; rdg (reading) contains a single reading within a textual variation. ^t09

N.B. the term lemma is used here in the text-critical sense of 'the reading accepted as that of the original or of the base text'. This sense differs from that in which the word is used elsewhere in the Guidelines, for example as in the attribute lemma where the intended sense is 'the root form of an inflected word', or 'the heading of an entry in a reference book, especially a dictionary'. ^t10

In recording readings within an apparatus entry, the rdg element should always be used; each app usually contains at least one rdg, though it may contain only notes. ^t11

The lem element may also be used to record the base text of the source edition, to mark the readings of a base witness, to indicate the preference of an editor or encoder for a particular reading, or (e.g. in the case of an external apparatus) to indicate precisely to which portion of the main text the variation applies. Those who prefer to work without the notion of a base text or who are not using the parallel segmentation method may prefer not to use it at all. How it is used depends in part on the method chosen for linking the apparatus to the text. ^t12

rdg (but not rdgGrp) is also a member of att.witnessed, which provides attributes used to identify the witnesses supporting a particular reading in a critical apparatus: wit (witness or witnesses) contains a space-delimited list of one or more pointers indicating the witnesses which attest to a given reading. ^t13

The wit attribute identifies the witnesses which have the reading in question. It is required if the apparatus gathers together readings from different witnesses, but may be omitted in an apparatus recording the readings of only one witness, e.g. substitutions, divergent opinions on what is in the witness or on how to expand abbreviations, etc. Even in such a one-witness apparatus, however, the wit attribute may still be useful when it is desired to record the occurrence of a particular reading in some other witness. ^t14

These elements also inherit the attributes resp (responsible party), which indicates the agency responsible for the intervention or interpretation, for example an editor or transcriber, and cert (certainty), which signifies the degree of certainty associated with the intervention or interpretation, from the att.global.responsibility class. As elsewhere, these attributes may be used to indicate the person responsible for the editorial decision being recorded, and also the degree of certainty associated with that decision by the person carrying out the encoding. ^t15

Because the hand attribute indicates a particular manuscript hand, it is intelligible only on a reading from a single witness. If an encoder wishes to indicate that a particular reading from a list in wit is in a particular hand, the witDetail element should be used. ^t16

Encoders should be aware of the distinct fields of use of the attribute values wit, hand, and source. Broadly, wit identifies the physical entity in which the reading is found (manuscript, clay tablet, papyrus, printed edition); hand refers to the agent responsible for inscribing that reading in that physical entity (scribe, author, inscriber, hand 1, hand 2); source indicates the scholar responsible for asserting the existence of that reading in that physical entity. In some cases, the categories may blur: a scholar may produce an edition introducing readings for which he or she is responsible; that edition may itself become a witness in a later critical apparatus. Thus, readings introduced as corrections in the earlier edition will be seen in the later apparatus as witnessed by the earlier edition. ^t17

### 13.1.4 Witness Information

A given reading is associated with the set of witnesses attesting it by listing the witnesses in the wit attribute on the rdg or lem element. Special mechanisms, described in the following sections, are needed to associate annotation on a reading with one specific witness among several (section 13.1.4.1 Witness Detail Information), to transcribe witness information verbatim from a source edition (section 13.1.4.2 Witness Information in the Source), and to identify the formal lists of witnesses typically provided in the front matter of critical editions (section 13.1.4.3 The Witness List). ^t18

#### 13.1.4.1 Witness Detail Information

When it is desired to give additional information about the reading of a particular witness or witnesses, such as noting that it appears in the margin or was corrected for the reading, that information may be given in a witDetail element. This is a specialized note, which can be linked to both a reading and to one or more of the witnesses for that reading. The link to the reading may be inferred from witDetail's position or made explicit by the target attribute which witDetail inherits from the attribute class att.pointing; the link to the witness, by the wit attribute. ^t19

Because it annotates an attribute value, witDetail cannot be included in the text at the point of attachment; without a target attribute, it refers to the closest preceding lem or rdg. But if there is any ambiguity or if the witDetail refers to multiple readings, target must be used to point to the reading(s) being annotated. ^t20

#### 13.1.4.2 Witness Information in the Source

Although witDetail provides a good way to annotate witness references in wit, lists of sigla may be complex enough that it is impractical to use the combination of wit and witDetail. Moreover, in the transcription of printed critical editions, it may be desirable to retain for future reference the exact form in which the source edition records the witnesses to a particular reading; this is particularly important in cases of ambiguity in the information, or uncertainty as to the correct interpretation. The wit element may be used to transcribe such lists of witnesses to a particular reading. ^t21

The wit list may appear following a rdg, rdgGrp, or lem element in any apparatus entry. wit may be used in a way functionally equivalent to the wit attribute if the sigla therein are wrapped in refs with target attributes pointing to a predefined witness. Because the wit attribute is more succinct, and because it makes the automated verification of correct witness references easier, using the wit attribute (with witDetail when needed) is almost always to be preferred. ^t22

#### 13.1.4.3 The Witness List

A list of all identified witnesses should normally be supplied in the front matter of the edition, or in the sourceDesc element of its header. This may be given either as a simple bibliographic list, using the listBibl element described in 3.12 Bibliographic Citations and References, or as a listWit element, which contains a series of witness elements. Each witness element may contain a brief characterization of the witness, given as one or more prose paragraphs. If more detailed information about a manuscript witness is available, it should be represented using the msDesc element provided by the msdescription module; an msDesc may appear within a listBibl. ^t23

Whether information about a particular witness is supplied by means of a bibl, msDesc, or witness element, a unique siglum for this source should always be supplied, using the global xml:id attribute. This identifier can then be used elsewhere to refer to this particular witness. ^t24

The minimal information provided by a witness list is thus the set of sigla for all the witnesses named in the apparatus. It is more helpful, however, for witness lists to be somewhat more informative: each witness element should contain at least a brief prose description of the witness, perhaps including a bibliographic citation. ^t25

### 13.1.5 Fragmentary Witnesses

If a witness is incomplete (whether a single fragment, a series of fragments, or a relatively complete text with one or more lacunae), it is usually desirable to record explicitly where its preserved portions begin and end. The empty tags witStart, witEnd, lacunaStart and lacunaEnd, which may occur within any lem or rdg element, indicate the beginning or end of a fragmentary witness or of a lacuna within a witness. ^t26

## 13.2 Linking the Apparatus to the Text

Three different methods may be used to link a critical apparatus to the text: the location-referenced method, the double-end-point-attached method, and the parallel segmentation method. ^t27

Both the location-referenced and the double end-point methods may be used with either in-line or external apparatus, the former dispersed within the base text, the latter held in some separate location, within or outside the document containing the base text. The parallel segmentation method may only be used for in-line apparatus. ^t28

Any document containing app elements requires a variantEncoding declaration in the encodingDesc element of its TEI header. The method attribute indicates which method is used to encode the apparatus of variants, and the location attribute indicates whether the apparatus appears within the running text or external to it. ^t29

### 13.2.1 The Location-referenced Method

The location-referenced method of encoding apparatus provides a convenient method for encoding printed apparatus; in this method as in most printed editions, the apparatus is linked to the base text by indicating explicitly only the block of text on which there is a variant (noted usually by a canonical reference scheme, or by line number in the edition, such as A 137 or Page 15 line 1). ^t30

When the apparatus is linked to the text by means of location references, it is not possible to find automatically the precise portion of text varied by the readings. In order to show explicitly what portion of the base text is replaced by the variant readings, the lem element may be used. ^t31

Where it is intended that the apparatus be complete enough to allow the reconstruction of the witnesses (or at least of their non-orthographic variations), simple location-reference methods are unlikely to be as successful as the other two methods, which allow the unambiguous reconstruction of the lemma from the encoding. ^t32

### 13.2.2 The Double End-Point Attachment Method

In the double end-point attachment method, the beginning and end of the lemma in the base text are both explicitly indicated. It thus differs from the location-referenced method, in which only the larger span of text containing the lemma is indicated. Double end-point attachment permits unambiguous matching of each variant reading against its lemma. It or the parallel-segmentation method should be used in all cases where this is desired, for example where the apparatus is intended to enable full reconstruction of the text, or of the substantives, of every witness. ^t33

When the double end-point attachment method is used, the from and to attributes of the app element are used to indicate the beginning and ending points of the reading in the base text: their values are identifiers which occur at the locations in question. If no other markup is present there, the beginning and ending points should be marked using the anchor element defined in chapter 17 Linking, Segmentation, and Alignment. In cases where it is not possible to insert anchors within the base text (e.g. where the text is on a read-only medium) the beginning and end of the lemma may be indicated by using the 'indirect pointing' mechanisms discussed in chapter 17. Explicit anchors are more likely to be reliable, and are therefore to be preferred. ^t34

The lemma need not be repeated within the app element in this method, as it may be extracted reliably from the base text. If an exhaustive list of witnesses is available, it will also not be necessary to specify just which manuscripts agree with the base text to enable reconstruction of witnesses. An application will be able to determine the manuscripts that witness the base reading, by noting which witnesses are attested as having a variant reading, and inferring the base text reading for all others after adjusting for fragmentary witnesses and for witnesses carrying overlapping variant readings. ^t35

This method is designed to cope with 'overlapping lemmata'. This method can readily cope with such difficult situations, typically found in large and complex traditions. The parallel segmentation method cannot handle overlaps among variants, and would require the individual variants to be split into pieces. ^t36

Because creation and interpretation of double end-point attachment apparatus will be lengthy and difficult it is likely that they will usually be created and examined by scholars only with mechanical assistance. ^t37

### 13.2.3 The Parallel Segmentation Method

This method differs from the double end-point attachment method in that all variants at any point of the text are expressed as variants on one another. In this method, no two variations can overlap, although they may nest. The texts compared are divided into matching segments all synchronized with one another. This permits direct comparison of any span of text in any witness with that in any other witness. With a positive apparatus, it is straightforward for an application to extract the full text of any one witness from the apparatus. ^t38

This method will (by definition) always be satisfactory when there are just two texts for comparison (assuming they are in the same language and script). It will however be less convenient for textual traditions where establishing a base text with variations from it is not a satisfactory goal for the edition, or in some cases where every detail of variation needs to be modeled. ^t39

In the parallel segmentation method, each segment of text on which there is variation is marked by an app element. If there is a preferred (or base) reading it is tagged with lem; each reading is given in a rdg element. ^t40

This method cannot be used with external apparatus: it must be used in-line. Note that apparatus encoded with this method may be translated into the double end-point attachment method and back without loss of information. Where double-end-point-attachment encodings have no overlapping lemmata, translation of these to the parallel segmentation encoding and back will also be possible without loss of information. ^t41

Parallel segmentation cannot, however, deal very gracefully with variants which overlap without nesting: such variants must be broken up into pieces in order to keep all witnesses synchronized. ^t42

### 13.2.4 Other Linking Methods

When an apparatus is provided it does not need to be given at the location in the transcription where the variation, emendation, attribution, or other apparatus observation occurs. Instead it may be stored in a separate place in the same file, or indeed in another file, and point to the location at which it is meant to be used. Storing apparatus entries separately can be beneficial when encoding multiple competing, potentially overlapping, interpretations of the same point in the source texts. ^t43

The location-referenced method can be used to point a position in a text using the loc attribute and a canonical reference that is understood and documented in the context of the file where it is used. Where possible it is recommended that other methods use the from attribute to point to an xml:id attribute on an anchor or other element at the location where the apparatus observation takes place. The contents of an element pointed to are understood to be equivalent to a lem if none exists in the app, and if a lem does exist this should replace any content. ^t44

The from attribute is a teidata.pointer datatype and thus contains a URI as a value. This means that it can point directly to an xml:id, an xml:id in another local file, or indeed a file identified by any URL or URN. ^t45

In addition, URLs can contain XPointer schemes including xpath(), range(), and string-range() which can be used in providing the location of an app that is stored separately from the text to which it applies. Both from and to can be used, as in the double end-point attachment method, to identify the starting and ending location for an apparatus using XPointer schemes described in 17.2.4 TEI XPointer Schemes section to more precisely identify this location where beneficial. ^t46

If only the from attribute is provided then it should be understood that this supplies the location of the textual variance that the apparatus documents. If the from attribute contains an XPointer scheme that identifies a range of text (or elements) then this is understood to record the starting and ending of the range as in the double end-point attachment method. In such a case a to attribute is unnecessary. ^t47

## 13.4 Strategies for Encoding Variation

Textual variation may manifest itself in many ways. Variation most frequently occurs at the phrase level, but is also common at higher structural levels, such as the verse line, paragraph, or chapter. When these structures are involved, some care must be taken in their encoding to ensure that TEI's Abstract Model is not being broken. It would be an error, for example, to have a div in the lem, but a p in a rdg inside the same apparatus entry, because these structures cannot occur at the same level. Similarly, it is an error if the contents of an apparatus entry place a p inside another p or an l inside an l. ^t48

Phenomena such as omissions and transpositions in witnesses will require some encoding strategies that differ from those in the examples above. An editor wishing to signal an omission in one witness should encode the omission using an empty rdg. If a witness contains an interpolation that the editor does not wish to show in the base text, an empty lem should be used, in the same fashion. ^t49

Transpositions are harder to encode, because they involve variation that occurs in different locations. A single app will therefore not be sufficient, and the variants must be linked. Both apps are linked via the exclude attribute, because they are mutually exclusive: if one reading is chosen for display in a reading interface, for example, the other must disappear and vice versa. To avoid repetition, the second pair of lines can make use of the copyOf attribute. ^t50

Apparatus entries may nest when there is variation at both higher and lower structural levels. ^t51
