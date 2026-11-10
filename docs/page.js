// The method page. index.html carries the complete English page and works without
// JavaScript. This module adds the German text (?lang=de), the language link, the dark-scheme
// toggle and the current section in the navigation. Copy buttons come from the shared
// assets/dhcraft/dhcraft-copy.js, which reads <html lang> after this module has set it, because
// module scripts run in document order. Prompts, commands and file names stay English, as the
// rule documents they address are, and carry lang="en" in the markup.

const LANG_STORE = "grounded-vault-lang";
const THEME_STORE = "grounded-vault-theme";
const TERMS = "https://github.com/DigitalHumanitiesCraft/grounded-vault/blob/main/knowledge/index.md";
const REPO = "https://github.com/DigitalHumanitiesCraft/grounded-vault/blob/main";

const SWITCH = {
  en: { to: "Deutsch", label: "Seite auf Deutsch anzeigen" },
  de: { to: "English", label: "Show this page in English" },
};

// German text by the data-t key of its element. Elements marked data-t-html receive inline
// markup (code, links) from this file only, never from data or the URL.
const PAGE_DE = {
  "skip": "Zum Inhalt",
  "nav.label": "Abschnitte",
  "nav.origin": "Herkunft",
  "nav.reuse": "Nachnutzung",
  "nav.example": "Beispiel",
  "nav.limits": "Grenzen",
  "nav.citation": "Zitation",
  "head.github": "Repository auf GitHub",
  "head.theme": "Dunkles Farbschema",

  "intro.lead": "Eine Repository-Architektur für Wissensbasen, in der jede inhaltliche Aussage einen maschinell auflösbaren Anker zu ihrer Quelle trägt, bis zur einzelnen Passage, Datenzeile oder Berechnung. KI-Agenten erzeugen diese Struktur, und die Architektur behauptet nicht, dass der Inhalt stimmt. Das Ergebnis ist ein Prüfobjekt für Menschen, die Berichte, Anträge oder Studien mit einem KI-Agenten schreiben und sie von Fachleuten Passage für Passage prüfen lassen müssen.",
  "figure.region": "Grafik der Provenienzkette, auf schmalen Bildschirmen seitlich scrollbar",
  "figure.alt": "Fünf Schichten, von einem Agenten gebaut, von oben nach unten Output, Assertions, Destillate, Markdown-Fassungen und Quellen, jede in der darunterliegenden verankert. Daneben drei Prüfungen, Validierung durch ein Skript, Maschinenprüfung durch ein zweites LLM und Verifikation durch einen Menschen, und die Statusleiter grounded, validated, verified. Die Beschriftung der Grafik ist englisch.",
  "figure.p1": `Ein KI-Agent baut die Kette von unten nach oben. Eine <a href="${TERMS}#source">Quelle</a> bleibt, wie sie ankam, und eine Publikation, deren Volltext nicht gespeichert werden darf, kommt als bibliografischer Eintrag hinein. Ihre <a href="${TERMS}#markdown-representation">Markdown-Fassung</a> wird einmal umgewandelt und nie mehr bearbeitet, mit einer <a href="${TERMS}#block-id">Block-ID</a> an jeder Passage, auf der eine Aussage ruhen könnte. Ein <a href="${TERMS}#distillate">Destillat</a> verdichtet eine Quelle zu Kernaussagen, jede mit einem Anker und einer Statement-ID. Eine <a href="${TERMS}#assertion">Assertion</a> formuliert einen Sachverhalt und ruht auf einer oder mehreren Kernaussagen, und ein <a href="${TERMS}#chapter">Kapitel</a> des Outputs versieht jeden tragenden Satz mit einer Fußnote auf eine Assertion. Ein eigener Schluss steht im Kapitel als <a href="${TERMS}#posit">Posit</a>, mit seiner Begründung und seiner offenen Belegfrage.`,
  "figure.p2": `Jeder Anker zeigt eine Schicht tiefer und löst maschinell auf. Dieses <a href="${TERMS}#grounding">Grounding</a> ist eine Struktur, die ein Agent herstellen kann, und sagt nichts darüber, ob eine Aussage stimmt. Die <span class="cat cat-validation">Validierung</span> durch <code>tools/validate.py</code> prüft Auflösbarkeit und Form. In der <span class="cat cat-review">Maschinenprüfung</span> beurteilt ein zweites Large Language Model (LLM), das nur das Paar sieht und nie die Überlegungen des erzeugenden Agenten, jede Aussage gegen die Stelle darunter. Die <span class="cat cat-verification">Verifikation</span> durch die als Verifikationsrolle benannte Person macht eine bestätigte Verbindung zum <a href="${TERMS}#evidence">Beleg</a>.`,
  "figure.p3": `Ein Status wird erst gesetzt, nachdem seine Prüfungen gelaufen sind, mit ihrem Datum in der Datei. Destillate und Assertions erreichen <code>validated</code> durch Validierung und Maschinenprüfung, ein Kapitel durch Validierung, sobald jede zitierte Assertion <code>validated</code> ist, und nur die Verifikation setzt <code>verified</code>. Ein Dokument steht nie höher als die Anker, auf denen es ruht, wie die <a href="${TERMS}#status-ladder">Statusleiter</a> festlegt, und die Verfahren stehen in <a href="${REPO}/knowledge/operations.md#check"><code>operations.md</code></a> (englisch).`,

  "origin.title": "Herkunft",
  "origin.p": `Grounded Vault ist ein Profil von <a href="https://dhcraft.org/Promptotyping/">Promptotyping</a> für Wissensarbeit unter Belegpflicht. Es übernimmt das gepflegte Projektwissen in <code>knowledge/</code> und ergänzt den Anker von jeder Aussage zu ihrer Quelle. Es schöpft aus der historischen Quellenkritik den relationalen Begriff des Belegs, aus der historischen Arbeitspraxis und den Nanopublikationen die mit ihrer Provenienz gepaarte Assertion, aus der digitalen Edition die Validierung eines Korpus gegen das eigene Schema und aus dem Datenmanagement Provenienz als maschinell durchlaufbare Relation, wie W3C PROV sie standardisiert. Das <a href="${REPO}/docs/concept.md">Konzeptpapier</a> (englisch) begründet die Architektur, und zitiert wird das Repository wie unter <a href="#citation">Zitation</a> angegeben.`,

  "reuse.title": "Nachnutzung",
  "reuse.lead": "Das Template braucht <a href=\"https://git-scm.com/downloads\">Git</a>, <a href=\"https://docs.astral.sh/uv/getting-started/installation/\">uv</a> und einen Coding-Agenten, der Dateien liest und schreibt, etwa <a href=\"https://code.claude.com/docs/en/setup\">Claude Code</a> oder Codex. <a href=\"https://obsidian.md\">Obsidian</a> ist optional, zum Verfolgen der Links.",
  "reuse.s1": "Repository anlegen",
  "reuse.s1.text": "Auf GitHub die Schaltfläche <a href=\"https://github.com/DigitalHumanitiesCraft/grounded-vault/generate\">„Use this template“</a> wählen und das neue Repository klonen.",
  "reuse.s2": "Installieren und validieren",
  "reuse.s2.text": "Ein frisches Template meldet <code>W-EMPTY</code>, <code>W-NO-OUTPUT</code> und <code>W-PLACEHOLDER</code>, bis Parameter und Inhalt eingetragen sind.",
  "reuse.s3": "Parameter mit dem Agenten setzen",
  "reuse.s3.text": "Der Agent fragt nach Zweck, Themen, Quelltypen, Genre, Sprache, Verifikationsrolle, Prüfmechanismus, Stilvorgaben und Harness-Regeln.",
  "reuse.s4": "Eine Quelle durch alle Schichten führen",
  "reuse.s4.text": "Zuerst ein Original in <code>00_sources/</code> ablegen, wo es standardmäßig außerhalb von Git bleibt. Ein vollständiger Durchlauf zeigt, ob die Regeln zum Material passen, bevor eine zweite Quelle dazukommt.",
  "label.shell": "Shell, in der Wurzel des Repositorys",
  "label.prompt": "Prompt",
  "label.reviewer": "Prompt für das prüfende LLM",

  "dl.title": "Dateien zum Herunterladen",
  "dl.svg": "die Grafik, für Paper und Folien",
  "dl.png": "die Grafik als Bild, 1600 mal 900",
  "dl.entry": "diese Seite, Titel und Grafik, 1600 mal 900",
  "dl.example": "das Beispiel, 1600 mal 900",
  "dl.all": "Alle Dateien mit dem Template-Repository (ZIP)",

  "example.title": "Beispiel an der Entity-Definition von PROV-DM",
  "example.lead": "Das Beispiel führt eine öffentliche Quelle, die Entity-Definition der <a href=\"https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-entity\">W3C-Empfehlung PROV-DM</a>, durch alle Schichten. Die Prompts der Reihe nach in einer frischen Kopie des Templates ausführen und jedes Ergebnis mit den Dateien in <a href=\"https://github.com/DigitalHumanitiesCraft/grounded-vault/tree/main/examples/prov-entity\"><code>examples/prov-entity/</code></a> vergleichen, deren IDs und Wortlaut die Dateien des eigenen Agenten nicht treffen müssen.",
  "ex.s1": "Für das Beispiel instanziieren",
  "ex.r1": "<code>knowledge/specification.md</code> mit den Parametern des Beispiels und die Topic Map <code>30_assertions/MOC-Provenance.md</code>.",
  "ex.s2": "Die Quelle aufnehmen",
  "ex.r2": "<code>10_markdown/documents/prov-entity.md</code>, die Definition als ein Absatz, der mit seiner Block-ID endet, im Beispiel <code>^entity-definition</code>.",
  "ex.s3": "Destillieren",
  "ex.r3": "<code>20_distillates/documents/prov-entity.md</code> mit einer Kernaussage, ihrem Anker <code>[[10_markdown/documents/prov-entity#^entity-definition]]</code> und der Statement-ID <code>^s1</code>.",
  "ex.s4": "Die Assertion bilden",
  "ex.r4": "<code>30_assertions/prov-entity-definition.md</code>, gegründet in <code>[[20_distillates/documents/prov-entity#^s1]]</code> und in der Topic Map verzeichnet.",
  "ex.s5": "Das Kapitel schreiben",
  "ex.r5": "<code>40_output/01-entity-definition.md</code>, ein Satz mit der Fußnote <code>Grounded in [[30_assertions/prov-entity-definition]]</code>, und der Validator meldet <code>CHAPTER READY</code>.",
  "ex.s6": "Die Paare exportieren",
  "ex.r6": "<code>prompts.jsonl</code> mit zwei Paaren, der Passage mit der Kernaussage und der Kernaussage mit der Assertion.",
  "ex.s7": "In einer eigenen Sitzung prüfen",
  "ex.s7.text": "<code>prompts.jsonl</code> in einen leeren Ordner außerhalb des Repositorys kopieren und dort eine Sitzung eines LLM einer anderen Modellfamilie starten.",
  "ex.r7": "<code>verdicts.jsonl</code>, eine Zeile je Paar, im Beispiel beide <code>fully supports</code>.",
  "ex.s8": "Die Urteile verbuchen",
  "ex.s8.text": "<code>verdicts.jsonl</code> in die Wurzel des Repositorys kopieren. Den zweiten Befehl erst ausführen, wenn der erste kein abweichendes Urteil meldet.",
  "ex.r8": "<code>checked.machine-review</code> mit Datum an Destillat und Assertion. Der Batch bleibt unter <code>checks/</code>, wie im Beispiel <code>checks/review-2026-10-03.jsonl</code>.",
  "ex.s9": "Den Status eintragen",
  "ex.r9": "Destillat und Assertion auf <code>validated</code> mit beiden Daten, das Kapitel auf <code>validated</code> mit seinem Validierungsdatum.",
  "ex.s10": "Verifikation",
  "ex.s10.text": "Die Verifikationsrolle liest die Assertion neben ihrer Passage und setzt, wo sie trägt, <code>status: verified</code> mit <code>checked.verification</code>. Im eingecheckten Beispiel ist dieser Schritt nicht erfolgt.",
  "ex.check": "Das eingecheckte Beispiel prüfen, in der Wurzel dieses Repositorys",

  "limits.title": "Grenzen, Lizenz und Zitation",
  "limits.check": "Die Architektur macht jede Aussage prüfbar und hält fest, wie weit sie geprüft ist. Ob eine Grounding-Relation als Beleg trägt, entscheidet allein die Verifikation.",
  "limits.grounding": "Ein frisch gebauter Vault enthält nur Grounding. Wo die Verifikation eine Stichprobe nimmt, sind nur die geprüften Verbindungen Belege.",
  "limits.review": "Die Maschinenprüfung ist probabilistisch und sortiert die Paare für die Verifikation vor. Empfohlen ist ein prüfendes LLM einer anderen Modellfamilie, und die Familie allein begründet noch keine Unabhängigkeit.",
  "limits.sentence": "Die Validierung findet einen Absatz ohne jede Fußnote. Einen ungestützten Satz in einem belegten Absatz findet nur das Lesen.",
  "limits.extension": "Bilder, deren Inhalt kein Text ist, und Code als Output sind benannte Erweiterungspunkte ohne ausgearbeiteten Anker.",
  "limits.licence": "Eigene Texte stehen unter <a href=\"https://github.com/DigitalHumanitiesCraft/grounded-vault/blob/main/LICENSE\">CC BY 4.0</a>, Code in <code>tools/</code>, <code>tests/</code> und ausführbaren Beispielen unter <a href=\"https://github.com/DigitalHumanitiesCraft/grounded-vault/blob/main/LICENSE-MIT\">MIT</a>, und der Auszug aus PROV-DM behält die W3C-Dokumentlizenz. Die gemeinsamen DHCraft-Dateien, das DHCraft-Logo und die Schriften behalten <a href=\"assets/dhcraft/LICENSE.md\">ihre eigenen Bedingungen</a>.",
  "limits.cite": "Zitation, Metadaten in <a href=\"https://github.com/DigitalHumanitiesCraft/grounded-vault/blob/main/CITATION.cff\"><code>CITATION.cff</code></a>",

  "foot.by": "Veröffentlicht von",
  "foot.licence": "Text CC BY 4.0, Code MIT, ausgenommen das DHCraft-Logo",
  "foot.source": "Quelle auf GitHub",
};

function stored(key) {
  try {
    return localStorage.getItem(key);
  } catch {
    return null;
  }
}

function store(key, value) {
  try {
    localStorage.setItem(key, value);
  } catch {
    // Storage can be blocked; the choice then holds for this visit only.
  }
}

function currentLang() {
  const asked = new URLSearchParams(location.search).get("lang");
  if (asked === "de" || asked === "en") return asked;
  return stored(LANG_STORE) === "de" ? "de" : "en";
}

function translate() {
  for (const node of document.querySelectorAll("[data-t]")) {
    const text = PAGE_DE[node.dataset.t];
    if (text === undefined) continue;
    if (node.hasAttribute("data-t-html")) node.innerHTML = text;
    else node.textContent = text;
  }
  for (const node of document.querySelectorAll("[data-t-label]")) {
    const text = PAGE_DE[node.dataset.tLabel];
    if (text !== undefined) node.setAttribute("aria-label", text);
  }
  for (const node of document.querySelectorAll("[data-t-alt]")) {
    const text = PAGE_DE[node.dataset.tAlt];
    if (text !== undefined) node.setAttribute("alt", text);
  }
}

function initLanguage(lang) {
  const other = lang === "en" ? "de" : "en";
  const link = document.getElementById("lang-switch");
  const url = new URL(location.href);
  url.searchParams.set("lang", other);
  link.href = url.search + url.hash;
  link.hreflang = other;
  link.lang = other;
  link.textContent = SWITCH[lang].to;
  link.setAttribute("aria-label", SWITCH[lang].label);
  link.hidden = false;
  link.addEventListener("click", () => store(LANG_STORE, other));
}

// The head script has already applied a stored choice; the toggle only flips and stores it.
function initTheme() {
  const root = document.documentElement;
  const button = document.getElementById("theme-toggle");
  const sync = () => button.setAttribute("aria-pressed", String(root.dataset.theme === "dark"));
  sync();
  button.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    store(THEME_STORE, root.dataset.theme);
    sync();
  });
}

function initNavState() {
  const links = new Map([...document.querySelectorAll(".site-nav a")].map((link) => [link.hash.slice(1), link]));
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const [id, link] of links) {
        if (id === entry.target.id) link.setAttribute("aria-current", "true");
        else link.removeAttribute("aria-current");
      }
    }
  }, { rootMargin: "-30% 0px -60% 0px" });
  for (const id of links.keys()) {
    const section = document.getElementById(id);
    if (section) observer.observe(section);
  }
}

const lang = currentLang();
document.documentElement.lang = lang;
if (lang === "de") translate();
initLanguage(lang);
initTheme();
initNavState();
