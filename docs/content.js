// All page text in English and German, so both languages carry the same statements.
// The example (a city archive's annual report and the board minutes behind one sentence)
// is synthetic. File names, block IDs and statement IDs follow knowledge/schema.md.
// Terms keep one translation throughout; the term list stands in docs/site-design.md.

const STORE = "grounded-vault-lang";

export const REPO = "https://github.com/DigitalHumanitiesCraft/grounded-vault";
const BLOB = `${REPO}/blob/main`;

export const LINKS = {
  useTemplate: `${REPO}/generate`,
  setupPrompt: `${BLOB}/SETUP.md#prompt-for-the-first-agent-session`,
  firstCycle: `${BLOB}/SETUP.md#first-production-cycle`,
  concept: `${BLOB}/docs/concept.md`,
  terminology: `${BLOB}/knowledge/index.md#terminology`,
  schema: `${BLOB}/knowledge/schema.md`,
  operations: `${BLOB}/knowledge/operations.md`,
  example: `${BLOB}/examples/prov-entity/README.md`,
  changelog: `${BLOB}/CHANGELOG.md`,
  licence: `${BLOB}/LICENSE`,
  uv: "https://docs.astral.sh/uv/getting-started/installation/",
  githubDesktop: "https://desktop.github.com/",
  pricing: "https://claude.com/pricing",
  git: "https://git-scm.com/downloads",
  claudeCode: "https://code.claude.com/docs/en/setup",
  claudeData: "https://code.claude.com/docs/en/data-usage",
  obsidian: "https://obsidian.md",
  docling: "https://github.com/docling-project/docling",
  promptotyping: "https://dhcraft.org/Promptotyping/",
  secondBrain: "https://github.com/chpollin/second-brain-vault",
};

// The five layers, top to bottom, as the trace walks them. Folder names are identifiers.
export const LAYERS = ["40_output", "30_assertions", "20_distillates", "10_markdown", "00_sources"];

// Per step: how many layers are reached, which status the statement holds, which layers carry
// a check result, and who acts. Text for each step is in TEXT[lang].trace.steps.
export const STEPS = [
  { id: "sentence", reach: 1, status: "grounded", actor: "reader" },
  { id: "assertion", reach: 2, status: "grounded", actor: "reader" },
  { id: "distillate", reach: 3, status: "grounded", actor: "reader" },
  { id: "passage", reach: 5, status: "grounded", actor: "reader" },
  { id: "validation", reach: 5, status: "grounded", actor: "script", marks: "resolves" },
  { id: "review", reach: 5, status: "validated", actor: "model", marks: "pair" },
  { id: "verification", reach: 5, status: "verified", actor: "person", marks: "verified" },
];

export const STATUSES = ["grounded", "validated", "verified"];

export const TEXT = {
  en: {
    switchTo: "Deutsch",
    switchLabel: "Seite auf Deutsch anzeigen",
    skip: "Skip to content",
    nav: { top: "Idea", start: "Start", notes: "Good to know" },
    template: "Template on GitHub",
    hero: {
      title: "Grounded Vault",
      lead: "Grounded Vault is a folder structure with written rules and checking scripts, kept in a Git repository, in which every sentence of a report links down to the passage of the source it rests on.",
      who: "For people who write reports, proposals or studies with an AI assistant and have to show where each statement comes from.",
      play: "Play the example",
      start: "Start a vault",
    },
    trace: {
      title: "Example: one sentence of an annual report, traced to its source",
      groups: { trace: "Trace down", machine: "Machine checks", person: "Human check" },
      prev: "Previous", play: "Play", pause: "Pause", next: "Next",
      done: "done", next_: "next",
      statusLabel: "Status of the assertion",
      statusGloss: { grounded: "linked by the assistant", validated: "checked by machines", verified: "confirmed by a person" },
      actors: { reader: "You follow the link", script: "Script", model: "Second language model", person: "Person" },
      layers: {
        "40_output": ["Report", "The finished text, one file per chapter."],
        "30_assertions": ["Assertion", "One statement per file, grounded in the distillates."],
        "20_distillates": ["Distillate", "What one source says, statement by statement."],
        "10_markdown": ["Markdown copy", "The source as text, converted once and never edited."],
        "00_sources": ["Original", "The file exactly as it arrived."],
      },
      excerpts: {
        "40_output": "The reading room reopened on 3 March 2025, after the roof repair.¹  `¹ Grounded in [[30_assertions/reading-room-reopened]]`",
        "30_assertions": "The reading room of the city archive reopened on 3 March 2025 after the roof repair.  `grounding: [[20_distillates/documents/board-minutes-2025-04#^s2]]`",
        "20_distillates": "The minutes record that the reading room has been open again since 3 March 2025, after the roof repair was completed.  `[[10_markdown/documents/board-minutes-2025-04#^b12]] ^s2`",
        "10_markdown": "4. The reading room has been open to the public again since 3 March 2025. The repair of the roof above the stacks was completed on 21 February.  `^b12`",
        "00_sources": "`board-minutes-2025-04.pdf`, minutes of the archive board meeting of 14 April 2025, kept unchanged.",
      },
      marks: {
        resolves: "anchor resolves",
        unchanged: "unchanged since conversion",
        original: "named as source of the copy",
        pair: "pair under review",
        verdict: "verdict: fully supports",
        verified: "confirmed by the verification role",
      },
      steps: {
        sentence: ["Sentence", "A sentence in the annual report carries a footnote. The footnote names the assertion the sentence rests on."],
        assertion: ["Assertion", "The assertion states the matter once, in a file of its own, and names the distillate statement that grounds it. A distillate belongs to one source, an assertion to the matter, so a second source, say the visitor statistics, can later join its grounding without the assertion changing."],
        distillate: ["Distillate", "The distillate condenses one source. Each of its statements carries an ID and exactly one anchor into the source text."],
        passage: ["Source passage", "The anchor points to paragraph ^b12 of the Markdown copy of the minutes. The copy was made once from the PDF and is never edited, so the passage stays where the anchor points. The AI assistant built this whole chain, and the status is grounded."],
        validation: ["Validation", "A script checks every link of the chain. Each anchor must lead to an existing passage, no layer may skip the one below it, and the Markdown copy must still be exactly the version that was converted. The script checks form. Whether the passage supports the sentence is left to the next step, so the status stays grounded."],
        review: ["Machine review", "A second language model sees only the passage and the statement built on it, never the reasoning of the assistant that wrote it, and answers with a verdict from a fixed list. Only “fully supports” passes, and the status becomes validated. Had the assistant used the February minutes, which only announce the reopening, the verdict on “has been open again” would be “overreaches”, and the statement would go back for rework."],
        verification: ["Verification", "The person named as verification role, here the head of the archive, reads the assertion next to the passages it rests on, confirms it and sets its status to verified with the date. Only this step sets verified, and only now does the vault count the link as evidence."],
      },
    },
    start: {
      title: "Start a vault",
      intro: "The template is the starting point. An AI assistant fills it in with you, and a script checks every step. Setting it up means typing a few commands in a terminal. If you have never done that, ask your assistant to run them for you, or ask a colleague for the first half hour.",
      toolsLabel: "You need",
      tools: [
        ["Git and a GitHub account", "free", LINKS.git],
        ["uv", "free, installs Python and the checking scripts", LINKS.uv],
        ["Claude Code or Codex", "paid plan or account", LINKS.claudeCode],
        ["Obsidian", "free, optional, for reading and following the links", LINKS.obsidian],
      ],
      copy: "Copy", copied: "Copied", copyFailed: "Copying failed, please select the text",
      steps: [
        { title: "Create your repository from the template", body: "On GitHub, choose “Use this template”. Then copy the new repository to your computer, which Git calls cloning. GitHub Desktop does this without a terminal.", action: ["Use this template", LINKS.useTemplate], links: [["GitHub Desktop", LINKS.githubDesktop]] },
        { title: "Install and run the checks", body: "Install uv, then open a terminal in the repository folder, install the environment and run the validator once. A fresh template reports warnings about placeholders and empty layers, which disappear as you fill it.", links: [["Install uv", LINKS.uv]], code: "uv sync --locked\nuv run python tools/validate.py ." },
        { title: "Set up the vault with the assistant", body: "Open the folder in your AI assistant and give it the first-session prompt from SETUP.md. It asks you, one question at a time, for the purpose, the topics, the source types, the language and the person who verifies.", prompt: "Instantiate this Grounded Vault template for my project. Follow the prompt for the first agent session in SETUP.md and ask me one question at a time.", links: [["SETUP.md", LINKS.setupPrompt]] },
        { title: "Carry one source through every layer", body: "Put one source into 00_sources/ and let the assistant take it all the way up, from Markdown copy to one written paragraph. One full pass shows whether the rules fit your material before a second source is touched.", prompt: "Take the source in 00_sources/[file] through one full production cycle as SETUP.md describes under First production cycle. Stop after each layer and show me the validator output.", links: [["First production cycle", LINKS.firstCycle]] },
        { title: "Let a second language model review the pairs", body: "The review tool writes each statement together with the passage it rests on as a short prompt into prompts.jsonl. Give these prompts to a language model from another provider than your assistant and save its answers, one verdict per pair, as verdicts.jsonl. The tool reads them back and records which pairs passed.", code: "uv run python tools/review.py emit . --out prompts.jsonl\nuv run python tools/review.py judge . --verdicts verdicts.jsonl" },
        { title: "Verify what matters", body: "The person named as verification role reads the assertions next to their passages. For each one confirmed, they set status in the head of its file to verified and enter the date under checked, by hand or by telling the assistant to do it. No script and no language model may set this status." },
      ],
    },
    notes: {
      title: "Good to know",
      limitsTitle: "What it does and does not do",
      limits: [
        "The vault does not make a statement true. It makes each statement checkable and shows how far it has been checked.",
        "A freshly built vault holds grounding only, links an assistant produced. Evidence exists once a person has verified a link.",
        "Your own conclusions are allowed. They enter the report as posits, marked with their reason and the open evidence question, so a reader sees where the text leaves its sources.",
        "Where sources contradict each other, both sides stay visible as contested until the verification role decides.",
        "Machine review can be wrong in both directions. It only sorts the pairs, so that human attention goes to those that survived it. Verification may cover a sample, and then only the sampled links count as evidence.",
      ],
      dataTitle: "Data, rights and costs",
      data: [
        ["Everything is plain Markdown in a Git repository on your computer. The template and its scripts are free, the text under CC BY 4.0 and the code under MIT.", LINKS.licence],
        ["The assistant has to read and write files in a folder, as Claude Code or Codex do. A chat in the browser is not enough. Assistant and reviewing language model run at a provider and read the files you let them read, and the provider's terms decide what happens to that text.", LINKS.claudeData],
        ["The costs are those of the assistant's plan and of the reviewing language model. The template adds none.", LINKS.pricing],
        ["Scans and PDFs enter as Markdown through a converter with text recognition such as Docling. Pages where tables or handwriting came out wrong need a look before distilling.", LINKS.docling],
        ["A publication whose full text may not be stored enters as a bibliographic record. Its anchor is then a verbatim quotation, checked character by character once at intake.", LINKS.schema],
        ["Licence and confidentiality are recorded on each source, so you can tell which full texts may be shared or published.", LINKS.schema],
      ],
      source: "details",
      furtherTitle: "Read further",
      further: [
        ["Worked example with a real source, the W3C provenance standard", LINKS.example],
        ["Concept paper, why the architecture is shaped as it is", LINKS.concept],
        ["Terminology, every term defined once", LINKS.terminology],
        ["Rules for the layers and the checks", LINKS.operations],
      ],
    },
    footer: {
      by: "A method by",
      license: "Text CC BY 4.0, code MIT.",
      example: "The archive, its report and its minutes in the example are invented.",
      related: "Related methods",
      repo: "Repository",
      changelog: "Changelog",
    },
  },

  de: {
    switchTo: "English",
    switchLabel: "Show this page in English",
    skip: "Zum Inhalt springen",
    nav: { top: "Idee", start: "Start", notes: "Gut zu wissen" },
    template: "Template auf GitHub",
    hero: {
      title: "Grounded Vault",
      lead: "Grounded Vault ist eine Ordnerstruktur mit schriftlichen Regeln und Prüfskripten in einem Git-Repository, in der jeder Satz eines Berichts bis zu der Quellstelle verlinkt ist, auf der er beruht.",
      who: "Für Menschen, die Berichte, Anträge oder Studien mit einem KI-Assistenten schreiben und zeigen müssen, woher jede Aussage stammt.",
      play: "Beispiel abspielen",
      start: "Vault anlegen",
    },
    trace: {
      title: "Beispiel: ein Satz aus einem Jahresbericht, zurückverfolgt bis zur Quelle",
      groups: { trace: "Zurückverfolgen", machine: "Maschinelle Prüfung", person: "Prüfung durch den Menschen" },
      prev: "Zurück", play: "Abspielen", pause: "Pause", next: "Weiter",
      done: "erledigt", next_: "folgt",
      statusLabel: "Status der Assertion",
      statusGloss: { grounded: "vom Assistenten verknüpft", validated: "maschinell geprüft", verified: "von einem Menschen bestätigt" },
      actors: { reader: "Du folgst dem Link", script: "Skript", model: "Zweites Sprachmodell", person: "Mensch" },
      layers: {
        "40_output": ["Bericht", "Der fertige Text, eine Datei je Kapitel."],
        "30_assertions": ["Assertion", "Eine Aussage je Datei, gestützt auf die Destillate."],
        "20_distillates": ["Destillat", "Was eine Quelle sagt, Aussage für Aussage."],
        "10_markdown": ["Markdown-Fassung", "Die Quelle als Text, einmal umgewandelt und nie mehr bearbeitet."],
        "00_sources": ["Original", "Die Datei genau so, wie sie ankam."],
      },
      excerpts: {
        "40_output": "Der Lesesaal öffnete am 3. März 2025 nach der Dachreparatur wieder.¹  `¹ Grounded in [[30_assertions/reading-room-reopened]]`",
        "30_assertions": "Der Lesesaal des Stadtarchivs öffnete am 3. März 2025 nach der Dachreparatur wieder.  `grounding: [[20_distillates/documents/board-minutes-2025-04#^s2]]`",
        "20_distillates": "Das Protokoll hält fest, dass der Lesesaal seit dem 3. März 2025 wieder geöffnet ist, nachdem die Dachreparatur abgeschlossen war.  `[[10_markdown/documents/board-minutes-2025-04#^b12]] ^s2`",
        "10_markdown": "4. Der Lesesaal ist seit dem 3. März 2025 wieder für das Publikum geöffnet. Die Reparatur des Dachs über dem Magazin wurde am 21. Februar abgeschlossen.  `^b12`",
        "00_sources": "`board-minutes-2025-04.pdf`, Protokoll der Sitzung des Archivbeirats vom 14. April 2025, unverändert aufbewahrt.",
      },
      marks: {
        resolves: "Anker löst auf",
        unchanged: "seit der Umwandlung unverändert",
        original: "als Quelle der Fassung genannt",
        pair: "Paar in der Prüfung",
        verdict: "Urteil: fully supports",
        verified: "von der Verifikationsrolle bestätigt",
      },
      steps: {
        sentence: ["Satz", "Ein Satz im Jahresbericht trägt eine Fußnote. Die Fußnote nennt die Assertion, auf der der Satz beruht."],
        assertion: ["Assertion", "Die Assertion formuliert den Sachverhalt einmal, in einer eigenen Datei, und nennt die Aussage im Destillat, auf die sie sich stützt. Ein Destillat gehört zu einer Quelle, eine Assertion zum Sachverhalt. Eine zweite Quelle, etwa die Besucherstatistik, kann deshalb später hinzukommen, ohne dass sich die Assertion ändert."],
        distillate: ["Destillat", "Das Destillat verdichtet eine Quelle. Jede seiner Aussagen trägt eine ID und genau einen Anker in den Quelltext."],
        passage: ["Quellstelle", "Der Anker zeigt auf Absatz ^b12 der Markdown-Fassung des Protokolls. Die Fassung wurde einmal aus dem PDF erzeugt und wird nie bearbeitet, deshalb bleibt die Stelle dort, wohin der Anker zeigt. Der KI-Assistent hat diese ganze Kette gebaut, der Status ist grounded."],
        validation: ["Validierung", "Ein Skript prüft jede Verbindung der Kette. Jeder Anker muss zu einer vorhandenen Stelle führen, keine Schicht darf die darunterliegende überspringen, und die Markdown-Fassung muss noch genau die umgewandelte Fassung sein. Das Skript prüft die Form. Ob die Stelle den Satz trägt, entscheidet der nächste Schritt, deshalb bleibt der Status grounded."],
        review: ["Maschinenprüfung", "Ein zweites Sprachmodell sieht nur die Stelle und die darauf gebaute Aussage, nie die Überlegungen des Assistenten, der sie geschrieben hat, und antwortet mit einem Urteil aus einer festen Liste. Nur „fully supports“ (stützt vollständig) besteht, und der Status wird validated. Hätte der Assistent das Februarprotokoll benutzt, das die Wiedereröffnung nur ankündigt, lautete das Urteil über „ist wieder geöffnet“ „overreaches“ (geht zu weit), und die Aussage ginge zur Überarbeitung zurück."],
        verification: ["Verifikation", "Die als Verifikationsrolle benannte Person, hier die Leitung des Archivs, liest die Assertion neben den Stellen, auf denen sie beruht, bestätigt sie und setzt ihren Status mit Datum auf verified. Nur dieser Schritt setzt verified, und erst jetzt zählt der Vault die Verbindung als Beleg."],
      },
    },
    start: {
      title: "Vault anlegen",
      intro: "Das Template ist der Ausgangspunkt. Ein KI-Assistent füllt es gemeinsam mit dir aus, und ein Skript prüft jeden Schritt. Zur Einrichtung gehören einige Befehle im Terminal. Wenn du das noch nie gemacht hast, lass sie den Assistenten ausführen oder hol dir für die erste halbe Stunde eine Kollegin oder einen Kollegen dazu.",
      toolsLabel: "Du brauchst",
      tools: [
        ["Git und ein GitHub-Konto", "kostenlos", LINKS.git],
        ["uv", "kostenlos, installiert Python und die Prüfskripte", LINKS.uv],
        ["Claude Code oder Codex", "kostenpflichtiger Plan oder Konto", LINKS.claudeCode],
        ["Obsidian", "kostenlos, optional, zum Lesen und Verfolgen der Links", LINKS.obsidian],
      ],
      copy: "Kopieren", copied: "Kopiert", copyFailed: "Kopieren fehlgeschlagen, bitte Text markieren",
      steps: [
        { title: "Repository aus dem Template erzeugen", body: "Wähle auf GitHub „Use this template“. Kopiere das neue Repository dann auf deinen Rechner, was Git Klonen nennt. GitHub Desktop erledigt das ohne Terminal.", action: ["Use this template", LINKS.useTemplate], links: [["GitHub Desktop", LINKS.githubDesktop]] },
        { title: "Installieren und die Prüfung laufen lassen", body: "Installiere uv, öffne ein Terminal im Ordner des Repositorys, installiere die Umgebung und starte den Validator einmal. Ein frisches Template meldet Warnungen zu Platzhaltern und leeren Schichten, die beim Ausfüllen verschwinden.", links: [["uv installieren", LINKS.uv]], code: "uv sync --locked\nuv run python tools/validate.py ." },
        { title: "Den Vault mit dem Assistenten einrichten", body: "Öffne den Ordner in deinem KI-Assistenten und gib ihm den Prompt für die erste Sitzung aus SETUP.md. Er fragt dich nacheinander nach Zweck, Themen, Quelltypen, Sprache und der Person, die verifiziert.", prompt: "Instantiate this Grounded Vault template for my project. Follow the prompt for the first agent session in SETUP.md and ask me one question at a time.", links: [["SETUP.md", LINKS.setupPrompt]] },
        { title: "Eine Quelle durch alle Schichten führen", body: "Lege eine Quelle in 00_sources/ ab und lass den Assistenten sie ganz nach oben bringen, von der Markdown-Fassung bis zu einem geschriebenen Absatz. Ein vollständiger Durchlauf zeigt, ob die Regeln zu deinem Material passen, bevor eine zweite Quelle dazukommt.", prompt: "Take the source in 00_sources/[file] through one full production cycle as SETUP.md describes under First production cycle. Stop after each layer and show me the validator output.", links: [["First production cycle", LINKS.firstCycle]] },
        { title: "Die Paare von einem zweiten Sprachmodell prüfen lassen", body: "Das Prüfwerkzeug schreibt jede Aussage zusammen mit der Stelle, auf der sie beruht, als kurzen Prompt in prompts.jsonl. Gib diese Prompts einem Sprachmodell eines anderen Anbieters als dein Assistent und speichere seine Antworten, ein Urteil je Paar, als verdicts.jsonl. Das Werkzeug liest sie zurück und hält fest, welche Paare bestanden haben.", code: "uv run python tools/review.py emit . --out prompts.jsonl\nuv run python tools/review.py judge . --verdicts verdicts.jsonl" },
        { title: "Verifizieren, worauf es ankommt", body: "Die als Verifikationsrolle benannte Person liest die Assertions neben ihren Stellen. Bei jeder bestätigten setzt sie im Kopf der Datei status auf verified und trägt unter checked das Datum ein, von Hand oder per Auftrag an den Assistenten. Kein Skript und kein Sprachmodell darf diesen Status setzen." },
      ],
    },
    notes: {
      title: "Gut zu wissen",
      limitsTitle: "Was der Vault leistet und was nicht",
      limits: [
        "Der Vault macht keine Aussage wahr. Er macht jede Aussage prüfbar und zeigt, wie weit sie geprüft ist.",
        "Ein frisch gebauter Vault enthält nur Grounding, also Verbindungen, die ein Assistent hergestellt hat. Ein Beleg entsteht erst, wenn ein Mensch eine Verbindung verifiziert hat.",
        "Eigene Schlüsse sind erlaubt. Sie stehen im Bericht als Posit, mit ihrer Begründung und der offenen Belegfrage, sodass man sieht, wo der Text seine Quellen verlässt.",
        "Wo Quellen einander widersprechen, bleiben beide Seiten als contested (strittig) sichtbar, bis die Verifikationsrolle entscheidet.",
        "Die Maschinenprüfung kann sich in beide Richtungen irren. Sie sortiert nur vor, damit menschliche Aufmerksamkeit auf die Paare fällt, die sie überstanden haben. Die Verifikation darf eine Stichprobe sein, dann zählen nur die geprüften Verbindungen als Beleg.",
      ],
      dataTitle: "Daten, Rechte und Kosten",
      data: [
        ["Alles ist einfaches Markdown in einem Git-Repository auf deinem Rechner. Template und Skripte sind kostenlos, der Text unter CC BY 4.0, der Code unter MIT.", LINKS.licence],
        ["Der Assistent muss Dateien in einem Ordner lesen und schreiben können, wie Claude Code oder Codex. Ein Chat im Browser reicht nicht. Assistent und prüfendes Sprachmodell laufen bei einem Anbieter und lesen die Dateien, die du ihnen gibst, und was mit diesem Text geschieht, regeln die Bedingungen des Anbieters.", LINKS.claudeData],
        ["Kosten entstehen durch den Plan des Assistenten und das prüfende Sprachmodell. Das Template selbst kostet nichts.", LINKS.pricing],
        ["Scans und PDFs kommen über einen Umwandler mit Texterkennung wie Docling als Markdown hinein. Seiten, auf denen Tabellen oder Handschrift misslungen sind, brauchen vor dem Destillieren einen Blick.", LINKS.docling],
        ["Eine Publikation, deren Volltext nicht gespeichert werden darf, kommt als bibliografischer Eintrag hinein. Ihr Anker ist dann ein wörtliches Zitat, das beim Aufnehmen einmal Zeichen für Zeichen geprüft wird.", LINKS.schema],
        ["Lizenz und Vertraulichkeit stehen bei jeder Quelle, sodass erkennbar ist, welche Volltexte geteilt oder veröffentlicht werden dürfen.", LINKS.schema],
      ],
      source: "Details",
      furtherTitle: "Weiterlesen",
      further: [
        ["Durchgerechnetes Beispiel mit einer echten Quelle, dem W3C-Provenienzstandard (englisch)", LINKS.example],
        ["Konzeptpapier, warum die Architektur so gebaut ist (englisch)", LINKS.concept],
        ["Terminologie, jeder Begriff einmal definiert (englisch)", LINKS.terminology],
        ["Regeln für die Schichten und die Prüfungen (englisch)", LINKS.operations],
      ],
    },
    footer: {
      by: "Eine Methode von",
      license: "Text CC BY 4.0, Code MIT.",
      example: "Archiv, Bericht und Protokoll im Beispiel sind erfunden.",
      related: "Verwandte Methoden",
      repo: "Repository",
      changelog: "Changelog",
    },
  },
};

export function currentLang() {
  const asked = new URLSearchParams(location.search).get("lang");
  if (asked === "de" || asked === "en") return asked;
  try {
    return localStorage.getItem(STORE) === "de" ? "de" : "en";
  } catch {
    return "en";
  }
}

export function rememberLang(lang) {
  try {
    localStorage.setItem(STORE, lang);
  } catch {
    // Storage can be blocked; the choice then holds for this visit only.
  }
}
