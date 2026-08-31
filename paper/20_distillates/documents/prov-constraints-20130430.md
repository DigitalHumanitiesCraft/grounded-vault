---
type: distillate
source-type: document
representation: "[[10_markdown/documents/prov-constraints-20130430]]"
topics: ["[[Verification]]", "[[Provenance]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: PROV-CONSTRAINTS (W3C Recommendation 2013-04-30)

The companion Recommendation to PROV-DM defines what validation of a provenance record means, and it fixes that meaning as internal consistency rather than as truth about the world.

## Core statements

- PROV-CONSTRAINTS complements the PROV-DM specification and defines a form of validation for provenance. [[10_markdown/documents/prov-constraints-20130430#^pc01]] ^s1
- A PROV instance is a set of PROV statements, and a PROV document consists of a toplevel anonymous instance together with zero or more named instances called bundles. [[10_markdown/documents/prov-constraints-20130430#^pc04]] ^s2
- PROV-DM imposes only minimal requirements upon PROV instances, and PROV instances need not be valid. [[10_markdown/documents/prov-constraints-20130430#^pc05]] ^s3
- A valid PROV instance corresponds to a consistent history of objects and interactions to which logical reasoning can be safely applied. [[10_markdown/documents/prov-constraints-20130430#^pc05]] ^s4
- The specification states that its notion of validity differs from the usual meaning of validity in logic and is closer to logical consistency. [[10_markdown/documents/prov-constraints-20130430#^pc05]] ^s5
- The specification defines four kinds of constraints that valid PROV instances must satisfy: uniqueness constraints, event ordering constraints, impossibility constraints, and type constraints. [[10_markdown/documents/prov-constraints-20130430#^pc06]] ^s6
- Validity and equivalence are defined in terms of normalization: definitions, inferences and uniqueness constraints normalize an instance, and event ordering, typing and impossibility constraints are then checked on the normal form. [[10_markdown/documents/prov-constraints-20130430#^pc07]] ^s7
- Validity and equivalence are specified procedurally by an algorithm based on normalization, and applications MAY implement the checks in any other way as long as the same instances are considered valid or equivalent. [[10_markdown/documents/prov-constraints-20130430#^pc08]] ^s8
- Checking validity or equivalence is RECOMMENDED but not required for applications compliant with PROV; producers SHOULD ensure that the provenance they produce is valid, and consumers MAY reject provenance that is not valid. [[10_markdown/documents/prov-constraints-20130430#^pc09]] ^s9
- Event ordering constraints require that the records in a PROV instance are consistent with a sensible ordering of the events relating the activities, entities and agents involved. [[10_markdown/documents/prov-constraints-20130430#^pc12]] ^s10
- Not all PROV-compliant applications need to perform inferences or check validity, but applications that create or transform provenance SHOULD attempt to produce valid provenance, so as to make it more useful to other applications by ruling out nonsensical or inconsistent information. [[10_markdown/documents/prov-constraints-20130430#^pc14]] ^s11
- The specification relates the common concepts and operations used throughout it to background terminology and ideas from logic, constraint programming and database constraints. [[10_markdown/documents/prov-constraints-20130430#^pc16]] ^s12
- The definitions, inferences and constraints can be viewed as pure logical assertions that could be checked in a variety of ways, and the procedural approach was adopted because it immediately demonstrates implementability and provides an adequate polynomial-time default implementation, whereas a purely declarative specification offers much less guidance for implementers. [[10_markdown/documents/prov-constraints-20130430#^pc17]] ^s13
- Before validation, equivalence checking or normalization, implementations should expand namespace prefixes and rewrite the instance so that co-referent identifiers are replaced by a single common identifier. [[10_markdown/documents/prov-constraints-20130430#^pc19]] ^s14
- The normal form of a PROV instance is the set of provenance statements resulting from applying all definitions, inferences and uniqueness constraints. [[10_markdown/documents/prov-constraints-20130430#^pc20]] ^s15
- The normalization algorithm terminates independently of the order in which inferences and constraints are applied, and produces a normal form that is unique up to isomorphism. [[10_markdown/documents/prov-constraints-20130430#^pc21]] ^s16
- A PROV instance is valid if its normal form exists and all validity constraints succeed on that normal form. [[10_markdown/documents/prov-constraints-20130430#^pc22]] ^s17
- A normal form of a PROV instance does not exist when a uniqueness constraint fails due to unification or merging failure. [[10_markdown/documents/prov-constraints-20130430#^pc23]] ^s18
- Two valid PROV instances are equivalent if they have isomorphic normal forms. [[10_markdown/documents/prov-constraints-20130430#^pc24]] ^s19
- Equivalence can also be checked over pairs of PROV instances that are not necessarily valid, subject to separately stated rules. [[10_markdown/documents/prov-constraints-20130430#^pc25]] ^s20
- Each bundle of a PROV document is handled independently, with no interaction between bundles when definitions, inferences or constraints are applied or when validity is checked. [[10_markdown/documents/prov-constraints-20130430#^pc27]] ^s21
- A PROV document is valid if each of its bundles is valid and no bundle identifier is repeated. [[10_markdown/documents/prov-constraints-20130430#^pc28]] ^s22

## Terms

- **Valid (PROV instance)**: an instance whose normal form exists and on which all validity constraints succeed; the term is used in the sense of logical consistency rather than the usual logical sense of validity. [[10_markdown/documents/prov-constraints-20130430#^pc05]]
- **PROV instance**: a set of PROV statements. [[10_markdown/documents/prov-constraints-20130430#^pc04]]
- **PROV document**: a toplevel anonymous instance together with zero or more named instances called bundles. [[10_markdown/documents/prov-constraints-20130430#^pc04]]
- **Normal form**: the instance resulting from applying all definitions, inferences and uniqueness constraints until none applies further. [[10_markdown/documents/prov-constraints-20130430#^pc20]]
- **Equivalence**: the relation between two valid instances that have isomorphic normal forms. [[10_markdown/documents/prov-constraints-20130430#^pc24]]

## Open questions

- The specification defines validity as internal consistency of a record and says nothing about whether the record corresponds to what actually happened, so it leaves open by what means that correspondence would be checked.
- Validity checking is only RECOMMENDED, and the specification does not say what a consumer is to do with provenance whose validity was never checked.
- The represented scope excludes the catalogues in sections 5 and 6, so the individual definitions, inferences and constraints are not covered here.

## Appraisal

The document is the piece of PROV that matters most for this vault, because it draws the line the vault also draws. Its notion of validity is a deterministic, machine-checkable property of a record, explicitly closer to consistency than to truth, and it says nothing about whether the described history occurred. That is precisely the relation between the vault's validation and its verification, so PROV-CONSTRAINTS supplies a standardized precedent for treating a formal check as necessary and insufficient. Its procedural style, an algorithm rather than a declarative semantics, with the declarative counterpart deferred to PROV-SEM, is also the style the vault's own validator follows, so the specification doubles as a model for how to write a checkable rule set. Its limits are those of its genre: it prescribes what a well-formed record looks like and offers nothing on how a record comes to be produced correctly.

## Related

- [[20_distillates/documents/prov-dm-20130430]]
