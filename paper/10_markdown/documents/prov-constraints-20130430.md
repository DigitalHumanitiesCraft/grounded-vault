---
type: representation
source-type: document
source: "[[00_sources/prov-constraints-20130430.html]]"
converter: "MarkItDown 0.1.6, then agent selection of the content-bearing sections; represented scope: 1 Introduction with 1.1 Conventions, 1.2 Purpose of this document, 1.3 Structure of this document and 1.4 Audience, the opening of 2.4 Validation Process Overview, and 7 Normalization, Validity, and Equivalence with 7.1 Instances and 7.2 Bundles and Documents. Abstract, status-of-this-document, table of contents, the remaining rationale subsections, compliance section, basic concepts, the full catalogues of definitions, inferences and constraints, glossary, termination proof, change log, acknowledgements and references are omitted."
channel: collection
metadata:
  title: "Constraints of the PROV Data Model"
  creator: "W3C Provenance Working Group"
  date: "2013-04-30"
  format: "html"
  identifier: "https://www.w3.org/TR/2013/REC-prov-constraints-20130430/"
  license: "W3C Document License (https://www.w3.org/Consortium/Legal/2002/copyright-documents-20021231)"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# Constraints of the PROV Data Model

W3C Recommendation 30 April 2013.

## 1. Introduction

Provenance is a record that describes the people, institutions, entities, and activities involved in producing, influencing, or delivering a piece of data or a thing. This document complements the PROV-DM specification [PROV-DM] that defines a data model for provenance on the Web. This document defines a form of validation for provenance. ^pc01

### 1.1 Conventions

The key words "*MUST*", "*MUST NOT*", "*REQUIRED*", "*SHALL*", "*SHALL NOT*", "*SHOULD*", "*SHOULD NOT*", "*RECOMMENDED*", "*MAY*", and "*OPTIONAL*" in this document are to be interpreted as described in [RFC2119]. ^pc02

In this document, logical formulas contain variables written as lower-case identifiers. Some of these variables are written beginning with the underscore character \_, by convention, to indicate that they appear only once in the formula. Such variables are provided merely as an aid to the reader. ^pc03

### 1.2 Purpose of this document

The PROV Data Model, PROV-DM, is a conceptual data model for provenance, which is realizable using different representations such as PROV-N and PROV-O. A PROV instance is a set of PROV statements. A PROV document consists of an anonymous instance, called the toplevel instance, together with zero or more named instances, called bundles. For example, a PROV document could be a .provn document, the result of a query, a triple store containing PROV statements in RDF, etc. ^pc04

The PROV-DM specification [PROV-DM] imposes minimal requirements upon PROV instances. A valid PROV instance corresponds to a consistent history of objects and interactions to which logical reasoning can be safely applied. PROV instances need not be valid. The term valid is chosen by analogy with notions of validity in other W3C specifications. This terminology differs from the usual meaning of "validity" in logic; our notion of validity of a PROV instance/document is closer to logical "consistency". ^pc05

This document specifies *definitions* of some provenance statements in terms of others, *inferences* over PROV instances that applications *MAY* employ, and also defines a class of valid PROV instances by specifying *constraints* that valid PROV instances must satisfy. There are four kinds of constraints: *uniqueness constraints*, *event ordering constraints*, *impossibility constraints*, and *type constraints*. Further discussion of the semantics of PROV statements, which justifies the definitions, inferences and constraints, and relates the procedural specification approach taken here to a declarative specification, can be found in the formal semantics [PROV-SEM]. ^pc06

We define validity and equivalence in terms of a concept called normalization. Definitions, inferences, and uniqueness constraints can be applied to normalize PROV instances, and event ordering, typing, and impossibility constraints can be checked on the normal form to determine validity. Equivalence of two PROV instances can be determined by comparing their normal forms. For PROV documents, validity and equivalence amount to checking the validity or pairwise equivalence of their respective instances. ^pc07

This specification defines validity and equivalence procedurally, via an algorithm based on normalization. Applications *MAY* implement validity and equivalence checking using normalization, as outlined here. Applications *MAY* also implement validation and equivalence checking in any other way as long as the same instances or documents are considered valid or equivalent, respectively. ^pc08

Checking validity or equivalence are *RECOMMENDED*, but not required, for applications compliant with PROV. Applications producing provenance *SHOULD* ensure that it is valid, and similarly applications consuming provenance *MAY* reject provenance that is not valid. Applications that are determining whether PROV instances or documents convey the same information *SHOULD* check equivalence as specified here. As a guideline, applications should treat equivalent instances or documents in the same way. This is a guideline only, because meaning of "in the same way" is application-specific. For example, applications that manipulate the syntax of PROV instances in particular representations, such as pretty-printing or digital signing, have good reasons to treat syntactically different, but equivalent, documents differently. ^pc09

### 1.3 Structure of this document

Section 2 gives a brief rationale for the definitions, inferences and constraints. Section 3 summarizes the requirements for compliance with this document, which are specified in detail in the rest of the document. Section 4 defines basic concepts used in the rest of the specification. ^pc10

Section 5 presents definitions and inferences. Definitions allow replacing shorthand notation in [PROV-N] with more explicit and complete statements; inferences allow adding new facts representing implicit knowledge about the structure of provenance. ^pc11

Section 6 presents four kinds of constraints, *uniqueness* constraints that prescribe that certain statements must be unique within PROV instances, *event ordering* constraints that require that the records in a PROV instance are consistent with a sensible ordering of events relating the activities, entities and agents involved, *impossibility* constraints that forbid certain patterns of statements in valid PROV instances, and *type* constraints that classify the types of identifiers in valid PROV instances. ^pc12

Section 7 defines the notions of validity, equivalence and normalization. ^pc13

### 1.4 Audience

The audience for this document is the same as for [PROV-DM]: developers and users who wish to create, process, share or integrate provenance records on the (Semantic) Web. Not all PROV-compliant applications need to perform inferences or check validity when processing provenance. However, applications that create or transform provenance *SHOULD* attempt to produce valid provenance, to make it more useful to other applications by ruling out nonsensical or inconsistent information. ^pc14

This document assumes familiarity with [PROV-DM] and employs the [PROV-N] notation. ^pc15

## 2.4 Validation Process Overview

*This section is non-normative.*

This section collects common concepts and operations that are used throughout the specification, and relates them to background terminology and ideas from logic [Logic], constraint programming [CHR], and database constraints [DBCONSTRAINTS]. This section does not attempt to provide a complete introduction to these topics, but it is provided in order to aid readers familiar with one or more of these topics in understanding the specification, and to clarify some of the motivations for choices in the specification to all readers. ^pc16

As discussed below, the definitions, inferences and constraints can be viewed as pure logical assertions that could be checked in a variety of ways. The rest of this document specifies validity and equivalence procedurally, that is, in terms of a reference implementation based on normalization. Although both declarative and procedural specification techniques have advantages, a purely declarative specification offers much less guidance for implementers, while the procedural approach adopted here immediately demonstrates implementability and provides an adequate (polynomial-time) default implementation. In this section we relate the declarative meaning of formulas to their procedural meaning. [PROV-SEM] provides an alternative, declarative characterization of validity which could be used as a starting point for other implementation strategies. ^pc17

## 7. Normalization, Validity, and Equivalence

We define the notions of normalization, validity and equivalence of PROV documents and instances. We first define these concepts for PROV instances and then extend them to PROV documents. ^pc18

Implementations should expand namespace prefixes and perform any appropriate reasoning about co-reference of identifiers, and rewrite the instance (by replacing co-referent identifiers with a single common identifier) to make this explicit, before doing validation, equivalence checking, or normalization. All of the following definitions assume that the application has already determined which URIs in the PROV instance are co-referent (e.g. owl:sameAs as a result of OWL reasoning). ^pc19

### 7.1 Instances

We define the normal form of a PROV instance as the set of provenance statements resulting from applying all definitions, inferences, and uniqueness constraints, obtained as follows: ^pc20

1. Apply all definitions to I by replacing each defined statement by its definition (possibly introducing fresh existential variables in the process), yielding an instance I1.
2. Apply all inferences to I1 by adding the conclusion of each inference whose hypotheses are satisfied and whose entire conclusion does not already hold (again, possibly introducing fresh existential variables), yielding an instance I2.
3. Apply all uniqueness constraints to I2 by unifying terms or merging statements and applying the resulting substitution to the instance, yielding an instance I3. If some uniqueness constraint cannot be applied, then normalization fails.
4. If no definitions, inferences, or uniqueness constraints can be applied to instance I3, then I3 is the normal form of I.
5. Otherwise, the normal form of I is the same as the normal form of I3 (that is, proceed by normalizing I3 at step 1).

Because of the potential interaction among definitions, inferences, and constraints, the above algorithm is iterative. Nevertheless, all of our constraints fall into a class of *tuple-generating dependencies* and *equality-generating dependencies* that satisfy a termination condition called *weak acyclicity* that has been studied in the context of relational databases [DBCONSTRAINTS]. Therefore, the above algorithm terminates, independently of the order in which inferences and constraints are applied. Appendix A gives a proof that normalization terminates and produces a unique (up to isomorphism) normal form. ^pc21

A PROV instance is valid if its normal form exists and all of the validity constraints succeed on the normal form. The following algorithm can be used to test validity: ^pc22

1. Normalize the instance I, obtaining normal form I'. If normalization fails, then I is not valid.
2. Apply all event ordering constraints to I' to build a graph G whose nodes are event identifiers and edges are labeled by "precedes" and "strictly precedes" relationships among events induced by the constraints.
3. Determine whether there is a cycle in G that contains a "strictly precedes" edge. If so, then I is not valid.
4. Apply the type constraints (section 5.3) to determine whether there are any violations of disjointness. If so, then I is not valid.
5. Check that none of the impossibility constraints (section 5.4) are violated. If any are violated, then I is not valid. Otherwise, I is valid.

A normal form of a PROV instance does not exist when a uniqueness constraint fails due to unification or merging failure. ^pc23

Two valid PROV instances are equivalent if they have isomorphic normal forms. That is, after applying all possible inference rules, the two instances produce the same set of PROV statements, up to reordering of statements and attributes within attribute lists, and renaming of existential variables. ^pc24

Equivalence can also be checked over pairs of PROV instances that are not necessarily valid, subject to the following rules: ^pc25

* If both are valid, then equivalence is defined above.
* If both are invalid, then equivalence can be implemented in any way provided it is reflexive, symmetric, and transitive.
* If one instance is valid and the other is invalid, then the two instances are not equivalent.

An application that processes PROV data *SHOULD* handle equivalent instances in the same way. This guideline is necessarily imprecise because "in the same way" is application-specific. Common exceptions to this guideline include, for example, applications that pretty-print or digitally sign provenance, where the order and syntactic form of statements matters. ^pc26

### 7.2 Bundles and Documents

The definitions, inferences, and constraints, and the resulting notions of normalization, validity and equivalence, work on a single PROV instance. In this section, we describe how to deal with general PROV documents, possibly including multiple named bundles as well as a toplevel instance. Briefly, each bundle is handled independently; there is no interaction between bundles from the perspective of applying definitions, inferences, or constraints, computing normal forms, or checking validity or equivalence. ^pc27

A PROV document is valid if each of the bundles I0, ..., In are valid and none of the bundle identifiers bi are repeated. ^pc28
