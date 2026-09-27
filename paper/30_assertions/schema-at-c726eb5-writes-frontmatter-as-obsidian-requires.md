---
type: assertion
topics: ["[[Architecture]]"]
status: grounded
checked:
  validation: 2026-09-27
grounding:
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s20]]"
contested-with: []
created: 2026-09-27
updated: 2026-09-27
---

# At commit c726eb5 of 2026-08-10, the Grounded Vault schema writes wikilink values quoted and block IDs unquoted in the frontmatter, as Obsidian requires for YAML

## Statement

In the schema document of the Grounded Vault profile at commit c726eb5 of 2026-08-10, each document type is specified by its frontmatter and, where one is fixed, its section skeleton, with fields required unless marked optional. In that frontmatter, wikilink values are quoted and block IDs are left unquoted, as Obsidian requires for YAML.

## Support

- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s20]], states the specification of each document type by frontmatter and skeleton and the quoting rule it follows for Obsidian

## Related

- [[30_assertions/block-references-address-blocks-as-literal-text-markers]]
- [[30_assertions/obsidian-stores-notes-as-plain-text-with-rebuildable-derived-state]]
