# Grounded Vault internal method manuscript

This directory is the canonical research instance for the internal Grounded Vault method manuscript. It consolidates the former German research blog and the planned English article into one English manuscript under [`40_output/grounded-vault-method.md`](40_output/grounded-vault-method.md).

The manuscript has no submission target. It develops the method for internal research use and preserves a fully traversable evidence chain. The Promptotyping paper remains a separate publication project and is the publication line intended for submission.

## Provenance

The research foundation was imported from the read-only source repository `chpollin/grounded-vault-paper` at commit `3045fb48b4ca4570498ff8628ca9995d40aa9374` on 21 August 2026. The imported `10_markdown/`, `20_distillates/`, `30_assertions/`, `glossary/`, `references/`, and `tools/analysis/` files retain their original bytes and anchors.

The former blog chapter `40_output/blog/blog-stuetzungsluecke-2026-08.md` remains in the source repository as a validated historical output. Its argument and empirical findings have been incorporated into the single manuscript in this directory. Future manuscript and knowledge changes belong here.

## Entry points

- [`HOME.md`](HOME.md) for the human reading path.
- [`CLAUDE.md`](CLAUDE.md) for the instance action layer.
- [`knowledge/specification.md`](knowledge/specification.md) for purpose, scope, status, and style.
- [`knowledge/journal.md`](knowledge/journal.md) for the migration and decision record.

## Checks

Run the instance checks from the repository root.

```text
python tools/inventory.py paper
python tools/validate.py paper
python tools/validate.py paper --chapter 40_output/grounded-vault-method.md
```

The root test suite continues to test the shared validator and its fixtures.

## Licence

The authored layers are licensed under Creative Commons Attribution 4.0 International. Markdown representations of third-party works retain the licence recorded in their metadata. The root repository licence does not override those source-specific terms.
