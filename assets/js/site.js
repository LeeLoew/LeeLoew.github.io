/* Lee Rogers — site behavior: nav toggle, scroll reveals, stat count-ups.
   Vanilla, ~90 lines, no dependencies. Final values are server-rendered, so
   no-JS and reduced-motion users always see complete content. */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* mobile nav */
  var toggle = document.querySelector(".nav-toggle");
  var header = document.getElementById("site-header");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* count-up: animate 0 → data-count, then restore exact server text */
  function countUp(el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var finalText = el.getAttribute("data-final") || el.textContent;
    if (isNaN(end)) return;
    var t0 = null;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / 900, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      if (p < 1) {
        el.textContent = Math.round(end * eased);
        requestAnimationFrame(step);
      } else {
        el.textContent = finalText;
      }
    }
    el.setAttribute("data-final", finalText);
    requestAnimationFrame(step);
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
      entry.target.querySelectorAll("[data-count]").forEach(countUp);
      if (entry.target.hasAttribute("data-count")) countUp(entry.target);
      io.unobserve(entry.target);
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -8% 0px" });
  els.forEach(function (el) { io.observe(el); });
})();
