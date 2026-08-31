---
type: assertion
topics: ["[[Provenance]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/prov-constraints-20130430#^s4]]"
  - "[[20_distillates/documents/prov-constraints-20130430#^s5]]"
  - "[[20_distillates/documents/prov-constraints-20130430#^s17]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s2]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# PROV validity is internal consistency

## Statement

PROV-CONSTRAINTS fixes the validity of a provenance record as a property of the record itself. A valid PROV instance corresponds to a consistent history of objects and interactions to which logical reasoning can be safely applied, and the specification says that this notion of validity differs from the usual meaning of validity in logic and is closer to logical consistency. Formally an instance is valid when its normal form exists and all validity constraints succeed on that normal form. PROV-DM treats the provenance of information as crucial for deciding whether information is to be trusted, how it should be integrated with other sources, and how credit is given to its originators.

## Support

- [[20_distillates/documents/prov-constraints-20130430#^s4]] — defines a valid instance as a consistent history open to logical reasoning
- [[20_distillates/documents/prov-constraints-20130430#^s5]] — marks the distance between this notion of validity and validity in logic
- [[20_distillates/documents/prov-constraints-20130430#^s17]] — gives the formal criterion, existence of the normal form plus success of all validity constraints
- [[20_distillates/documents/prov-dm-20130430#^s2]] — supplies the role of provenance as an input to trust, integration and credit decisions

## Related

- [[30_assertions/prov-models-entities-activities-agents]]
- [[30_assertions/prov-derivation-conditions-unspecified]]
