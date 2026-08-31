---
type: distillate
source-type: publication
reference: "obsidianhelpdatastorage"
topics: ["[[Architecture]]"]
status: validated
checked:
  quote: 2026-08-10
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Obsidian Help, How Obsidian stores data

The Obsidian help page on data storage states what a vault physically is, that notes are plain text files a foreign editor may touch, and that the metadata Obsidian keeps about those files is a cache that can be rebuilt from them.

## Core statements

- Obsidian stores notes as Markdown-formatted plain text files in a vault. ^s1
  > "Obsidian stores your notes as [[Basic formatting syntax|Markdown-formatted]] plain text files in a _vault_." (obsidianhelpdatastorage, How Obsidian stores data, § lead)
- A vault is a folder on the local file system, including any subfolders. ^s2
  > "A vault is a folder on your local file system, including any subfolders." (obsidianhelpdatastorage, How Obsidian stores data, § lead)
- Because the notes are plain text files, other text editors and file managers can edit and manage them, and Obsidian refreshes the vault to keep up with such external changes. ^s3
  > "Because notes are plain text files, you can use other text editors and file managers to edit and manage notes. Obsidian automatically refreshes your vault to keep up with any external changes." (obsidianhelpdatastorage, How Obsidian stores data, § lead)
- Internal links are local to a vault, which is why Obsidian recommends against creating vaults within vaults. ^s4
  > "Because [[Internal links]] are local to a vault, we recommend that you don't create vaults within vaults." (obsidianhelpdatastorage, How Obsidian stores data, § lead, callout "Vaults within vaults")
- Obsidian creates an `.obsidian` configuration folder in the root folder of the vault, holding the preferences specific to that vault. ^s5
  > "Obsidian creates an `.obsidian` [[configuration folder]] in the root folder of the vault, which contains preferences specific to that vault, such as [[hotkeys]], [[themes]], and [[community plugins]]." (obsidianhelpdatastorage, How Obsidian stores data, § Vault settings)
- Obsidian uses IndexedDB, a low-level client-side database, as backend storage, where it helps maintain the state of Obsidian Sync connections and preserves the metadata cache while the application is closed. ^s6
  > "IndexedDB is a low-level, client-side database that Obsidian uses for backend storage. It helps maintain the state of [[Introduction to Obsidian Sync|Obsidian Sync]] connections, and preserves the [[#Metadata cache]] when the application is closed." (obsidianhelpdatastorage, How Obsidian stores data, § IndexedDB)
- Obsidian maintains a local record of metadata about the files of the vault, called the metadata cache, in order to provide a fast experience while using the app. ^s7
  > "In order to provide a fast experience while using the app, Obsidian maintains a local record of metadata about the files in your vault called the **metadata cache**." (obsidianhelpdatastorage, How Obsidian stores data, § IndexedDB > Metadata cache)
- The metadata cache powers many parts of the app, among them the Graph view and the Outline view. ^s8
  > "This metadata powers many things across the app, from the Graph view to the Outline view." (obsidianhelpdatastorage, How Obsidian stores data, § IndexedDB > Metadata cache)
- The metadata cache can fall out of sync with the underlying files, and it can then be rebuilt from the app settings. ^s9
  > "Obsidian keeps this cache in sync with the files in your vault, but it is possible for the data to get out of sync with the underlying files. In the event that this happens to your vault, you can rebuild your metadata cache from the app settings in the *Files and links* section." (obsidianhelpdatastorage, How Obsidian stores data, § IndexedDB > Metadata cache)
- When Apple's Lockdown Mode is enabled and Obsidian is not excluded from it, the database files do not save and Obsidian reindexes at every start. ^s10
  > "If Apple's [Lockdown Mode](<https://support.apple.com/en-us/105120>) is enabled and Obsidian is not excluded, these database files will not save, requiring reindexing each time the app starts." (obsidianhelpdatastorage, How Obsidian stores data, § IndexedDB, callout)

## Terms

- **vault**: a folder on the local file system, including any subfolders, in which Obsidian stores the notes as plain text files
  > "A vault is a folder on your local file system, including any subfolders." (obsidianhelpdatastorage, How Obsidian stores data, § lead)
- **metadata cache**: the local record of metadata about the files of the vault that Obsidian maintains for speed and can rebuild from those files
  > "In order to provide a fast experience while using the app, Obsidian maintains a local record of metadata about the files in your vault called the **metadata cache**." (obsidianhelpdatastorage, How Obsidian stores data, § IndexedDB > Metadata cache)

## Open questions

- The page says that notes are plain text files and that IndexedDB serves as backend storage for sync state and the metadata cache; it does not say which of the two holds a given piece of information when the two disagree beyond the rebuild remedy.
- The page names the rebuild of the metadata cache as the remedy for a cache out of sync, without saying what triggers such a divergence or how a user detects one.

## Appraisal

The page is user-facing product documentation of the vendor, so it describes the intended behaviour of one version of one application and carries no independent verification. Its value for this vault is that it is the operator's own statement on the two properties the vault depends on, storage in plain files a foreign tool may write and a derived index that can be discarded and rebuilt. Its limit is genre, since a help page states no version, no guarantee and no schema of the cached metadata, so nothing here can be held against a future release.

## Related

- [[20_distillates/publications/obsidian-docs-metadatacache]]
- [[30_assertions/MOC-Architecture]]
