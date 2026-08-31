---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/publications/obsidian-help-data-storage#^s1]]"
  - "[[20_distillates/publications/obsidian-help-data-storage#^s2]]"
  - "[[20_distillates/publications/obsidian-help-data-storage#^s3]]"
  - "[[20_distillates/publications/obsidian-help-data-storage#^s6]]"
  - "[[20_distillates/publications/obsidian-help-data-storage#^s7]]"
  - "[[20_distillates/publications/obsidian-help-data-storage#^s9]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# Obsidian stores notes as plain text files beside a rebuildable metadata cache

## Statement

Obsidian stores notes as Markdown-formatted plain text files in a vault, and a vault is a folder on the local file system including any subfolders. Because the notes are plain text files, other text editors and file managers can edit and manage them, and the application refreshes the vault to keep up with such external changes. Beside the files the application maintains a local record of metadata about them, the metadata cache, which serves speed of use and is preserved in a client-side database while the application is closed. The vendor states that this record can fall out of sync with the underlying files and that it can then be rebuilt from the app settings.

## Support

- [[20_distillates/publications/obsidian-help-data-storage#^s1]] — states the storage form, Markdown-formatted plain text files in a vault
- [[20_distillates/publications/obsidian-help-data-storage#^s2]] — defines the vault as a folder on the local file system
- [[20_distillates/publications/obsidian-help-data-storage#^s3]] — states that foreign editors may write the files and that the application follows such changes
- [[20_distillates/publications/obsidian-help-data-storage#^s6]] — names the client-side database that preserves the metadata cache while the application is closed
- [[20_distillates/publications/obsidian-help-data-storage#^s7]] — defines the metadata cache as a local record of metadata about the files
- [[20_distillates/publications/obsidian-help-data-storage#^s9]] — states that the cache can fall out of sync with the files and can be rebuilt

## Related

- [[30_assertions/plain-text-meets-archival-format-criteria]]
- [[30_assertions/obsidian-link-registers-map-files-to-files]]
