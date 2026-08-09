# Feldbericht: Die KISUG-Schreibwelle als Belastungstest des Templates

Stand 2026-08-09. Rückmeldung aus der Instanz `kisug-wissensbasis` (privates Repo) an das Template, nach der ersten vollständigen Runde aus Abfrage-Betrieb, Prüfwellen-Buchung und neuer Kapitelprosa mit blinder Doppelprüfung. Fallstudien-Details bleiben hier anonymisierbar knapp; die Instanz-Journale tragen die Genese.

## Was das Template geleistet hat

**Die Statusleiter erzwingt Ehrlichkeit, und `E-LADDER` ist ihr wirksamster Fehlercode.** 27 offene Leiter-Fehler der Instanz ließen sich nur durch eine echte zweite Machine Review auflösen; der Lauf fand dabei zwei Teilstützungen und eine Überdehnung, die seit Wochen als `validated` mitliefen (eine Assertion machte aus einer Quellenaussage "derzeit nicht relevant" ein "derzeit nicht erreichbar"). Ohne die Leiterregel wäre das nie wieder angefasst worden.

**Die blinde Zweitprüfung findet Autorenfehler des Betreibers selbst.** In derselben Runde hat die blinde Review zwei frisch angelegte Assertions der betreuenden Session geprüft und drei Überdehnungen im eigenen Text gefunden (unverankerter Nenner, Inhalt aus dem nicht ankerfähigen Offene-Fragen-Abschnitt, Folgerungssatz im Assertionskörper). Der Wert der Trennung von Produktion und Prüfung ist damit am Betreiber demonstriert und hängt nicht an der Schwäche Dritter.

**Die Zitatprüfkette unterscheidet Fassungen.** Der Abgleich gegen lokal beschaffte Volltexte fand ein Distillat, dessen Zitate der arXiv-Fassung folgten, während die Referenz auf die Verlagsfassung zeigt; zwei Formulierungen wichen ab. Zugleich hat eine Stichprobe des Hauptstrangs einen Fehlbefund des Prüfagenten widerlegt (eine angebliche Leerzeichen-Abweichung, die die Verlagsfassung nicht trägt). Die Schichtung aus Agentenprüfung und Hauptstrang-Stichprobe fängt beide Fehlerrichtungen.

**Die Provenienzkette zahlt sich im Abfrage-Betrieb aus.** Ein Gesamtbericht über 44 interne Quellen ließ sich mit Trägerschicht je Aussage schreiben, und sieben tragende Befunde waren in Minuten gegen die Distillat-Anker verifizierbar, weil jeder Anker direkt ansteuerbar ist. Eine adversariale Nachprüfung desselben Berichts fand 13 Abweichungen bei rund 215 Angaben; auch diese Prüfung war nur möglich, weil die Anker existieren.

**Kapitelprosa auf fertiger Aussagen-Schicht ist schnell und bleibt prüfbar.** Das erste neue Kapitel der Instanz entstand in einem Zug auf 28 bestehenden Assertions, und die beiden blinden Reviews (Ankertreue, Faktencheck) lieferten zusammen 24 präzise, behebbare Befunde. Der Fußnotenvertrag macht die Reviews mechanisch prüfbar; kein Befund war Geschmacksurteil.

## Wo das Template Lücken gezeigt hat

Jede Lücke ist ein konkreter heutiger Vorfall, kein hypothetisches Risiko.

1. **Dubletten-Erkennung fehlt.** Die betreuende Session hat eine Assertion angelegt, die mit identischer Grounding-Menge (vier gleiche Anker) bereits existierte; gefunden hat es erst die blinde Review, gelöscht wurde per Hand. Vorschlag: ein Validator- oder Lint-Check, der Assertion-Paare mit identischer oder fast identischer Grounding-Menge als Warnung meldet (etwa `W-DUPLICATE-GROUNDING`). Das ist billig zu prüfen und hätte den Fall maschinell gefangen.
2. **Register-Drift ist unsichtbar.** Die Status-Spalte des Inventarregisters der Instanz wich in 36 Zeilen vom realen Frontmatter-Status der Distillate ab, als stiller Rest früherer Buchungswellen. Vorschlag: ein Check, der die Statusangaben der `state`-Tabellen gegen die Frontmatter der verlinkten Dateien abgleicht (etwa `W-REGISTER-DRIFT`).
3. **Alias-Drift in Fußnoten.** Neun Fußnoten-Aliase des neuen Kapitels kürzten die Assertion-Titel, teils um genau die einschränkende Klausel; gefunden hat es die menschengeführte Review. Vorschlag: ein Lint-Vergleich des Alias-Textes von `Grounded in`-Fußnoten gegen den H1-Titel der Zieldatei (Warnung bei Abweichung).
4. **Der Offene-Fragen-Abschnitt der Distillate ist ein Anker-Schatten.** Befunde, die dort stehen, sind nicht zitierfähig, tragen aber oft genau die Einschränkungen, die eine Assertion braucht; in der Instanz musste eine Aussage deshalb zurückgebaut werden, obwohl der Inhalt im Distillat steht. Vorschlag zur Diskussion: entweder eine Konvention, prüfbare Befunde per additivem Anker in die Core statements zu heben, oder ein eigener ankerfähiger Befund-Abschnitt.
5. **Werkzeugpfade in Instanz-Steuerdokumenten driften.** Die Instanz-CLAUDE.md nannte einen Validator-Pfad, der nur im Template existiert; aufgefallen ist es erst einem Prüfagenten. Der bestehende Altpfad-Check von `migrate.py` ließe sich um dokumentierte Kommandozeilen in CLAUDE.md erweitern.

## Einordnung

Die Instanz steht nach der Runde bei vier Validator-Fehlern, die sämtlich auf ein einziges noch unbeschafftes Quellwerk zurückgehen, bei null Lint-Fehlern ohne undeklarierte Warnung, und jede tragende Aussage der neuen Prosa ist über die Kette bis zur Quellstelle rückverfolgbar. Dass die verbliebenen Fehler exakt die reale Weltlücke abbilden (ein fehlendes PDF) und nichts sonst, ist das Verhalten, für das die Architektur gebaut wurde. Die fünf Lücken oben sind Werkzeuglücken am Rand der Kette; die Kette selbst hat in jeder Prüfrichtung gehalten.
