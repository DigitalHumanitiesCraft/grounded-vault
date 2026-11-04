// The playable example: one report sentence traced down the five layers, then checked by a
// script, a second language model and a person. Each step is a complete state, so any step
// can be shown directly; play only advances through them.

import { LAYERS, STATUSES, STEPS } from "./content.js";

// Autoplay leaves time to read: a fixed minimum plus a share per word of the caption.
const MIN_DELAY = 6000;
const PER_WORD = 260;

export function h(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (key === "class") node.className = value;
    else if (key === "text") node.textContent = value;
    else node.setAttribute(key, value);
  }
  node.append(...children.filter((child) => child !== null && child !== undefined && child !== ""));
  return node;
}

/** Text with `backtick` spans rendered as code, built from text nodes only. */
function richText(value) {
  // A code span after prose is an anchor or ID and gets the class that sets it apart.
  return value.split("`").map((part, index, parts) => {
    if (!(index % 2)) return document.createTextNode(part);
    return h("code", { class: parts[index - 1] ? "anchor" : "", text: part });
  });
}

/** The check result each layer shows in a given step, keyed by layer. */
function marksFor(step, t) {
  const m = t.marks;
  switch (step.marks) {
    case "resolves":
      return { "40_output": m.resolves, "30_assertions": m.resolves, "20_distillates": m.resolves, "10_markdown": m.unchanged, "00_sources": m.original };
    case "pair":
      return { "20_distillates": m.verdict, "10_markdown": m.pair };
    case "verified":
      return { "30_assertions": m.verified };
    default:
      return {};
  }
}

export function createTrace(host, text) {
  const t = text.trace;
  const stepButtons = [];
  const groups = [["trace", STEPS.slice(0, 4)], ["machine", STEPS.slice(4, 6)], ["person", STEPS.slice(6)]];
  const stepNav = h("div", { class: "trace-steps" }, ...groups.map(([group, steps]) => h("div", { class: "step-group" },
    h("p", { class: "step-group-label", text: t.groups[group] }),
    h("ol", {}, ...steps.map((step) => {
      const index = STEPS.indexOf(step);
      const [title] = t.steps[step.id];
      const state = h("span", { class: "visually-hidden" });
      const button = h("button", { type: "button", class: `step-pill actor-${step.actor}`, "data-index": String(index) },
        h("span", { class: "step-no", "aria-hidden": "true", text: String(index + 1) }), h("span", { text: title }), state);
      button.addEventListener("click", () => show(index, true));
      stepButtons.push({ button, state });
      return h("li", {}, button);
    })))));

  const ladder = h("ol", { class: "ladder", "aria-label": t.statusLabel },
    ...STATUSES.map((status) => h("li", { "data-status": status },
      h("span", { class: "status-value", text: status }), h("span", { class: "status-gloss", text: t.statusGloss[status] }))));

  const rows = LAYERS.map((layer) => {
    const [name, gloss] = t.layers[layer];
    const mark = h("span", { class: "mark" });
    const excerpt = h("p", { class: "excerpt" }, ...richText(t.excerpts[layer]));
    const row = h("li", { class: "layer", "data-layer": layer },
      h("span", { class: "knot", "aria-hidden": "true" }),
      h("div", { class: "layer-body" },
        h("p", { class: "layer-head" }, h("strong", { text: name }), " ", h("code", { text: `${layer}/` })),
        h("p", { class: "layer-gloss", text: gloss }),
        excerpt,
        mark));
    return { row, excerpt, mark, body: row.querySelector(".layer-body") };
  });
  const column = h("ol", { class: "layers" }, ...rows.map(({ row }) => row));

  const caption = h("p", { class: "trace-caption", "aria-live": "polite" });
  const prev = h("button", { type: "button", class: "btn", text: t.prev });
  const play = h("button", { type: "button", class: "btn primary", text: t.play });
  const next = h("button", { type: "button", class: "btn", text: t.next });
  const controls = h("div", { class: "trace-controls" }, prev, play, next);

  // The caption sits under the layer it explains; the controls stay at the foot of the figure.
  host.replaceChildren(h("p", { class: "trace-title", text: t.title }), stepNav, ladder, column, controls);

  let index = 0;
  let timer = 0;

  function show(target, stopPlaying = false, follow = true) {
    if (stopPlaying) stop();
    index = Math.max(0, Math.min(target, STEPS.length - 1));
    const step = STEPS[index];
    stepButtons.forEach(({ button, state }, position) => {
      const phase = position < index ? "done" : position === index ? "current" : "next";
      button.dataset.phase = phase;
      if (phase === "current") button.setAttribute("aria-current", "step");
      else button.removeAttribute("aria-current");
      state.textContent = phase === "done" ? `, ${t.done}` : phase === "next" ? `, ${t.next_}` : "";
    });
    const marks = marksFor(step, t);
    let anchor = rows[0];
    rows.forEach((entry, position) => {
      const { row, mark } = entry;
      row.dataset.reached = position < step.reach ? "yes" : "no";
      // In the trace phase the layer just reached is current; while checking, every layer with a result is.
      const current = step.marks ? Boolean(marks[LAYERS[position]]) : position === step.reach - 1 || (step.id === "passage" && position >= 3);
      row.dataset.current = current ? "yes" : "no";
      if (current) anchor = entry;
      mark.textContent = marks[LAYERS[position]] || "";
      row.dataset.mark = step.marks && marks[LAYERS[position]] ? step.marks : "";
    });
    const reached = STATUSES.indexOf(step.status);
    [...ladder.children].forEach((item, position) => {
      item.dataset.phase = position < reached ? "done" : position === reached ? "current" : "next";
    });
    host.dataset.actor = step.actor;
    const [title, body] = t.steps[step.id];
    caption.replaceChildren(h("strong", { text: `${t.actors[step.actor]}. ${title}. ` }), body);
    anchor.body.append(caption);
    if (follow) keepInView();
    prev.disabled = index === 0;
    next.disabled = index === STEPS.length - 1;
  }

  // Keep the caption between the sticky header and the sticky controls. scrollIntoView with
  // scroll margins left some captions under the controls in Chromium, so the offset is computed.
  function keepInView() {
    const box = caption.getBoundingClientRect();
    const top = (document.getElementById("site-head")?.getBoundingClientRect().bottom ?? 0) + 12;
    const bottom = controls.getBoundingClientRect().top - 12;
    if (box.bottom > bottom) window.scrollBy({ top: Math.min(box.bottom - bottom, box.top - top), behavior: "instant" });
    else if (box.top < top) window.scrollBy({ top: box.top - top, behavior: "instant" });
  }

  function delay() {
    const words = caption.textContent.split(/\s+/).length;
    return Math.max(MIN_DELAY, words * PER_WORD);
  }

  function stop() {
    clearTimeout(timer);
    timer = 0;
    play.textContent = t.play;
  }

  function tick() {
    if (index >= STEPS.length - 1) return stop();
    show(index + 1);
    timer = setTimeout(tick, delay());
  }

  function start(fromBeginning = false) {
    play.textContent = t.pause;
    show(fromBeginning || index >= STEPS.length - 1 ? 0 : index + 1);
    timer = setTimeout(tick, delay());
  }

  play.addEventListener("click", () => (timer ? stop() : start()));
  prev.addEventListener("click", () => show(index - 1, true));
  next.addEventListener("click", () => show(index + 1, true));
  show(0, false, false);
  return { start, stop, show };
}
