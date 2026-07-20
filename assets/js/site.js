/* Lee Rogers — site behavior: nav toggle + scroll reveals.
   Vanilla, no dependencies. Reveal styling is gated on the `js` class set
   inline in the head; a CSS fallback animation un-hides everything after
   ~1.2s even if this file never loads, so content can't be stranded. */
(function () {
  "use strict";

  document.documentElement.classList.add("js-ready");

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* mobile nav */
  var toggle = document.querySelector(".nav-toggle");
  var header = document.getElementById("site-header");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && header.classList.contains("nav-open")) {
        header.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* reveals */
  var els = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    els.forEach(function (el) { el.classList.add("is-in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("is-in");
      io.unobserve(entry.target);
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -8% 0px" });
  els.forEach(function (el) { io.observe(el); });
})();
