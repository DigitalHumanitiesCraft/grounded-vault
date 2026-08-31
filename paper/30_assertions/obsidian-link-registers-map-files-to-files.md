---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/publications/obsidian-docs-metadatacache#^s2]]"
  - "[[20_distillates/publications/obsidian-docs-metadatacache#^s3]]"
  - "[[20_distillates/publications/obsidian-docs-metadatacache#^s4]]"
  - "[[20_distillates/publications/obsidian-docs-metadatacache#^s5]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# Obsidian link registers map files to files

## Statement

The two link registers of the metadata cache are stated in the API reference as mappings between files. The property holding all resolved links maps the path of each source file to an object of destination file paths with the link count, and the property holding all unresolved links maps each source file to an object of unknown destinations with count, whose source paths are vault absolute paths as in the resolved register. Both registers carry the declared type of a mapping from string to a mapping of string to number, which gives two levels of key and a count. Both registers key on file paths, and their declared types provide no further level.

## Support

- [[20_distillates/publications/obsidian-docs-metadatacache#^s2]] — states the resolved register as a mapping of source file path to destination file paths with count
- [[20_distillates/publications/obsidian-docs-metadatacache#^s3]] — states the unresolved register as a mapping of source file to unknown destinations with count
- [[20_distillates/publications/obsidian-docs-metadatacache#^s4]] — gives the declared type of both registers, two string levels and a number
- [[20_distillates/publications/obsidian-docs-metadatacache#^s5]] — states that the source paths of the unresolved register are vault absolute paths

## Related

- [[30_assertions/obsidian-stores-notes-as-plain-text-with-rebuildable-derived-state]]
- [[30_assertions/block-references-address-blocks-as-literal-text-markers]]
