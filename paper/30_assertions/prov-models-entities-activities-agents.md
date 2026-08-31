---
type: assertion
topics: ["[[Provenance]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/prov-dm-20130430#^s10]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s11]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s12]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s13]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s21]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s22]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s23]]"
  - "[[20_distillates/documents/prov-dm-20130430#^s24]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# PROV models provenance as entities, activities, and agents

## Statement

The PROV data model describes provenance through three core types and the relations that hold between them. Entities are things with some fixed aspects, activities occur over a period of time and act upon or with entities, and agents bear responsibility. At the core of PROV, provenance describes the use and production of entities by activities, which agents may influence in various ways, and all core relations are binary and named in the past tense so that they express what happened. On top of this the model carries a layer of responsibility with three named relations, attribution ascribing an entity to an agent, association assigning responsibility for an activity to an agent with a role in it, and delegation assigning authority and responsibility to an agent acting on behalf of another agent that retains some responsibility for the outcome.

## Support

- [[20_distillates/documents/prov-dm-20130430#^s10]] — states the core of PROV as the use and production of entities by activities under the influence of agents
- [[20_distillates/documents/prov-dm-20130430#^s11]] — gives the relational form of the model, binary core relations in the past tense
- [[20_distillates/documents/prov-dm-20130430#^s12]] — defines the type entity
- [[20_distillates/documents/prov-dm-20130430#^s13]] — defines the type activity
- [[20_distillates/documents/prov-dm-20130430#^s21]] — defines the type agent through the responsibility it bears
- [[20_distillates/documents/prov-dm-20130430#^s22]] — supplies attribution as the ascribing of an entity to an agent
- [[20_distillates/documents/prov-dm-20130430#^s23]] — supplies association as the assignment of responsibility for an activity
- [[20_distillates/documents/prov-dm-20130430#^s24]] — supplies delegation as the assignment of authority and responsibility to a representative

## Related

- [[30_assertions/prov-validity-is-internal-consistency]]
- [[30_assertions/prov-derivation-conditions-unspecified]]
