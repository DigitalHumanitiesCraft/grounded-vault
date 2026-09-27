---
type: glossary
term: "provenance"
created: 2026-08-10
updated: 2026-09-27
---

# Provenance

The origin history of a statement made persistent and machine-resolvable. In this vault it takes the form of the provenance chain, which the Grounded Vault terminology at commit `79cd1d3` defines as the unbroken anchor path from an output sentence through assertions and distillates to source locations, in which a break anywhere is a defect that validation detects. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx19]]

The W3C PROV data model defines provenance more broadly as a record that describes the people, institutions, entities and activities involved in producing, influencing or delivering a piece of data or a thing. [[10_markdown/documents/prov-dm-20130430#^dm01]] PROV leaves granularity open and records derivation as an asserted influence without defining its conditions. The vault fixes granularity at the block anchor and makes resolvability a checked property. Both positions agree that provenance informs trust decisions and asserts nothing about the truth of content. Whether an anchored location actually supports its statement is decided on the judgment side, where [[glossary/grounding]] becomes [[glossary/evidence]].
