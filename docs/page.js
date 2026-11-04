// The method page: language, header, hero with the playable trace, start steps, notes and
// footer. All text comes from content.js; the page loads no data files.

import { currentLang, LINKS, REPO, rememberLang, TEXT } from "./content.js";
import { createTrace, h } from "./trace.js";

const NAV = ["top", "start", "notes"];

function renderHeader(t, lang) {
  const other = lang === "en" ? "de" : "en";
  // A plain link, so the other language is addressable without the script; the click only remembers it.
  const url = new URL(location.href);
  url.searchParams.set("lang", other);
  const toggle = h("a", { class: "lang", href: url.search + url.hash, "aria-label": t.switchLabel, hreflang: other, lang: other, text: t.switchTo });
  toggle.addEventListener("click", () => rememberLang(other));
  document.getElementById("site-head").replaceChildren(
    h("a", { class: "brand", href: "#top" },
      h("img", { src: "assets/dhcraft-mark-white.svg", alt: "", width: "28", height: "28" }),
      h("span", { text: "Grounded Vault" })),
    h("nav", { class: "site-nav", "aria-label": t.nav.top },
      h("ul", {}, ...NAV.map((id) => h("li", {}, h("a", { href: `#${id}`, text: t.nav[id] }))))),
    h("div", { class: "head-actions" }, toggle, h("a", { class: "pill", href: REPO, "aria-label": t.template },
      h("span", { class: "long", text: t.template }), h("span", { class: "short", "aria-hidden": "true", text: "GitHub" }))),
  );
  document.querySelector(".skip").textContent = t.skip;
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
  }, { rootMargin: "-40% 0px -55% 0px" });
  for (const id of links.keys()) {
    const section = document.getElementById(id);
    if (section) observer.observe(section);
  }
}

function renderHero(t, onPlay) {
  const play = h("button", { type: "button", class: "btn primary", text: t.hero.play });
  play.addEventListener("click", onPlay);
  document.getElementById("hero-text").replaceChildren(
    h("h1", { text: t.hero.title }),
    h("p", { class: "lead", text: t.hero.lead }),
    h("p", { class: "who", text: t.hero.who }),
    h("p", { class: "actions" }, play, h("a", { class: "btn", href: "#start", text: t.hero.start })),
  );
}

function copyButton(t, value) {
  // Without the Clipboard API the prompt stays selectable text and no button appears.
  if (!navigator.clipboard?.writeText) return null;
  const copy = h("button", { type: "button", class: "btn small", text: t.copy });
  copy.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(value);
      copy.textContent = t.copied;
    } catch {
      copy.textContent = t.copyFailed;
    }
    setTimeout(() => {
      copy.textContent = t.copy;
    }, 2500);
  });
  return copy;
}

function renderStart(t) {
  const s = t.start;
  const tools = h("div", { class: "tools" }, h("h3", { text: s.toolsLabel }),
    h("ul", {}, ...s.tools.map(([name, note, href]) => h("li", {}, h("a", { href, text: name }), `, ${note}`))));
  const steps = s.steps.map((step) => h("li", {},
    h("h3", { text: step.title }),
    h("p", { text: step.body }),
    step.action ? h("p", {}, h("a", { class: "btn primary", href: step.action[1], text: step.action[0] })) : null,
    step.code ? h("div", { class: "prompt-box" }, h("pre", { class: "prompt code" }, h("code", { text: step.code })), copyButton(s, step.code)) : null,
    step.prompt ? h("div", { class: "prompt-box" }, h("pre", { class: "prompt" }, h("code", { text: step.prompt })), copyButton(s, step.prompt)) : null,
    step.links ? h("p", { class: "step-links" }, ...step.links.map(([label, href]) => h("a", { href, text: label }))) : null));
  document.getElementById("start-body").replaceChildren(
    h("h2", { text: s.title }),
    h("p", { class: "intro", text: s.intro }),
    tools,
    h("ol", { class: "steps" }, ...steps),
  );
}

function renderNotes(t) {
  const n = t.notes;
  document.getElementById("notes-body").replaceChildren(
    h("h2", { text: n.title }),
    h("div", { class: "columns" },
      h("section", {}, h("h3", { text: n.limitsTitle }),
        h("ul", { class: "plain" }, ...n.limits.map((sentence) => h("li", { text: sentence })))),
      h("section", {}, h("h3", { text: n.dataTitle }),
        h("ul", { class: "plain" }, ...n.data.map(([sentence, href]) => h("li", {}, `${sentence} `, h("a", { href, text: n.source })))))),
    h("section", { class: "further" }, h("h3", { text: n.furtherTitle }),
      h("ul", {}, ...n.further.map(([label, href]) => h("li", {}, h("a", { href, text: label }))))),
  );
}

function renderFooter(t) {
  const f = t.footer;
  document.getElementById("site-foot").replaceChildren(
    h("div", { class: "foot-grid" },
      h("div", {},
        h("p", {}, `${f.by} `, h("a", { href: "https://dhcraft.org", text: "Digital Humanities Craft" }), `. ${f.license}`),
        h("p", { class: "quiet", text: f.example })),
      h("ul", { class: "foot-links" },
        h("li", {}, h("a", { href: REPO, text: f.repo })),
        h("li", {}, h("a", { href: LINKS.changelog, text: f.changelog }))),
      h("ul", { class: "foot-links", "aria-label": f.related },
        h("li", {}, h("a", { href: LINKS.promptotyping, text: "Promptotyping" })),
        h("li", {}, h("a", { href: LINKS.secondBrain, text: "Second Brain Vault" })))),
  );
}

function main() {
  const lang = currentLang();
  const t = TEXT[lang];
  document.documentElement.lang = lang;
  renderHeader(t, lang);
  const trace = createTrace(document.getElementById("trace"), t);
  renderHero(t, () => {
    trace.start(true);
    document.getElementById("trace").scrollIntoView({ block: "nearest" });
  });
  renderStart(t);
  renderNotes(t);
  renderFooter(t);
  initNavState();
  if (location.hash) document.querySelector(location.hash)?.scrollIntoView();
}

main();
