# Plan: Bau des Template-Repositorys

Dieses Dokument steuert den Bau des Grounded-Vault-Template-Repositorys. Die konzeptuelle Grundlage ist `concept.md`, die Kurzform `onepager.md`. Referenzmaterial sind die KISUG-Wissensbasis (gewachsene Instanz, `knowledge/domaenenwissen.md` als Schema-Vorbild) und die Promptotyping-Vorlagen im Obsidian-Vault (`Vault Operations/Templates/Promptotyping/`).

## Getroffene Entscheidungen

- Name: Grounded Vault, Repo `grounded-vault`.
- Sprache des Templates durchgehend Englisch; instanziierte Inhalte tragen ihre eigene Projektsprache. Anspruch: sehr gut dokumentiert, so kompakt und elegant wie möglich.
- Sechs `knowledge/`-Dokumente (index, specification, schema, operations, state, journal) plus Splitregel.
- Source Types als offene Typologie (archivable documents als Regelfall, citable-only publications als Randfall, structured data; images als benannter, unausgearbeiteter Erweiterungspunkt), Beschaffungskanäle orthogonal, Deep Research als Referenzkanal.
- Jede Quellrepräsentation trägt einen kompakten DC-kompatiblen Metadatenblock (title, creator, date, type, identifier, license) plus Kanal-Vermerk; Lizenz und Vertraulichkeit sind Quellen-Metadaten, keine Architekturmechanik.
- Statusprogression `grounded` / `validated` / `verified` plus `contested`; drei Prüfinstanzen Validation, Machine Review, Verification.
- **Prüfvertrag statt Prüfwerkzeug**: invariant ist je Instanz der Vertrag (Gegenstand, Autoritätsgrenze, Bedingungen, protokolliertes Ergebnis samt Datum am Dokument); der Mechanismus ist Instanziierungsentscheidung. Das Template liefert den generischen Validator, einsteckbare Checks je Source Type und für Machine Review den Vertrag mit Referenz-Promptgerüst.
- **Audit trail** (vormals audit ledger): Statusfelder plus Check-Datum-Felder am Dokument; Dokumentstatus ist das Minimum seiner Anker-Stände.
- Quellen-Versionierung durch Ersetzung: Repräsentation nach Konversion unveränderlich, neue Version als neue Datei mit Datumssuffix-Slug, altes Distillat wird als superseded markiert.
- Anker-Vertrag statt fixer Fußnotenpflicht: Inline-Marker plus strukturierter Frontmatter-Spiegel, Fußnote als Referenznotation für Prosa.
- Bibliografisches Format CSL-JSON.
- Frontmatter-Feldnamen strikt aus der Konzept-Terminologie abgeleitet (`grounding`, `source-type`, `status`, `checked`).
- Repräsentationsschicht als ein Ordner `00_representation/` mit Untertypen-Ordnern, spiegelbildlich zu `10_distillates/`.
- Frontend und Code-Deliverable außerhalb des ersten Wurfs.

## Arbeitspakete

1. **Repo-Skelett.** Ordnerstruktur laut `concept.md` Sektion 10, `.gitignore` (mindestens `_sources/`), README als englische Kurzfassung des Konzepts, `concept.md` als `docs/concept.md` übernehmen.
2. **`schema.md`-Vorlage.** Der Kern des Templates. Generalisierte Dokumenttypen mit exaktem Frontmatter- und Sektionsskelett je Typ (representation, distillate je Source Type, claim, deliverable chapter, glossary entry, topic map), Metadatenblock, kontrollierte Wertelisten, Anker-Vertrag, Audit-Trail-Felder, Platzhalter für das Themen-Rückgrat. Vorbild ist KISUGs Typen-Katalog, übersetzt und um die Strom-Spezifika bereinigt.
3. **Übrige `knowledge/`-Vorlagen.** index (Navigation, Begriffslexikon aus concept Sektion 3), specification (Zweck-Gerüst mit Parametern), operations (die Ketten: acquire je Kanal inkl. Deep-Research-Prompt-Gerüst, ingest, distill mit dreistufiger Erzeugungskette, claim-building, chapter-writing, query, checking mit den drei Prüfverträgen und dem Machine-Review-Promptgerüst), state (Inventar- und Registertabellen leer), journal (Eintragsformat).
4. **Action-Layer und Einstieg.** `CLAUDE.md`-Vorlage mit Sessionstart-Lesereihenfolge, Routing-Tabelle und explizit austauschbarem Harness-Block; `HOME.md`-Vorlage für den menschlichen Einstieg.
5. **Validierung.** `tools/validate.py` generisch gegen das Schema: Frontmatter-Konformität je Typ, Ankerauflösung (Block-Refs), Zitat-Identität wo ein Volltext vorliegt, Berechnungsanker (Deklarationsprüfung, Nachrechnung als optionaler Lauf), MOC-Erreichbarkeit, beidseitige contested-Relationen, Text/Frontmatter-Spiegelabgleich im Deliverable, Statusdisziplin (Status nur mit passenden `checked`-Einträgen). Python-Style-Skill anwenden; Tests gegen beide Beispielinstanzen.
6. **Beispielinstanzen.** `examples/minimal/` valide, mit je einer Quelle pro Source Type, einem Distillat je Quelle, einem Claim (gemischt gestützt), einem Deliverable-Absatz mit Fußnote und Setzung. Daneben `examples/broken/` mit je einem Exemplar der Defektklassen (toter Block-Ref, verwaister Claim, einseitige contested-Relation, schemawidriges Frontmatter, Fußnote ohne Schlüsselwort, Status ohne Check-Eintrag); die Tests beweisen, dass der Validator jeden Defekt fängt.
7. **Instanziierung.** `SETUP.md` mit den Parametern (Thema und Rückgrat, aktive Source Types, Deliverable-Genre, Sprache, Verifikationsrolle, Prüfmechanismen) und der Ausfüllreihenfolge der Vorlagen; optional ein Setup-Skill als Nachlieferung.
8. **Veröffentlichung.** GitHub-Repository anlegen, als Template-Repository markieren, Verbindung zur Promptotyping-Dokumentation herstellen. Sichtbarkeit und Lizenz sind Operator-Entscheidungen vor dem Push (Empfehlung: CC BY für Doku und Vorlagen, MIT für `tools/`).

Baureihenfolge: 1, dann 2, 5 und 6 verschränkt (jede Schema-Regel bekommt sofort ihr Fixture und ihren Check), dann 3, 4, 7, 8.

## Offene Entscheidungen

| Entscheidung | Optionen | Stand |
|---|---|---|
| Lizenz | CC BY für Doku, MIT für tools/ (Empfehlung) oder einheitlich | Operator, vor Veröffentlichung |
| Sichtbarkeit | public ab Start oder erst nach Review der Beispielinstanz | Operator |
| Setup-Skill | Nachlieferung nach SETUP.md | am Ende von Paket 7 |
| Verhältnis zur Vault-Konvention | Verweis aus [[Konvention Promptotyping Documents]] auf das Profil | echte Vault-Session nötig |

## Related

- `concept.md` (englische Vollform)
- `onepager.md` (deutsche Synthese)
- KISUG: `knowledge/domaenenwissen.md`, `knowledge/verarbeitung.md`, `knowledge/verifikation.md`
- Vault: `Vault Operations/Templates/Promptotyping/`, [[Konvention Projekt-Wissensdokument]]
