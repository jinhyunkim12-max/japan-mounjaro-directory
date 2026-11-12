(function () {
  var input = document.getElementById("clinic-search");
  var cards = Array.prototype.slice.call(document.querySelectorAll(".clinic-card"));
  var sections = Array.prototype.slice.call(document.querySelectorAll(".city-section"));
  var controls = Array.prototype.slice.call(document.querySelectorAll("[data-city-filter]"));
  var empty = document.getElementById("filter-empty");
  var form = document.querySelector(".finder");
  var city = "all";

  function paint() {
    controls.forEach(function (control) {
      var selected = control.getAttribute("data-city-filter") === city;
      if (control.tagName === "BUTTON") control.setAttribute("aria-pressed", selected ? "true" : "false");
      control.classList.toggle("is-on", selected);
    });
  }

  function apply() {
    var query = ((input && input.value) || "").trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (card) {
      var cityOk = city === "all" || card.getAttribute("data-city") === city;
      var text = (card.getAttribute("data-search") || "").toLowerCase();
      var ok = cityOk && (!query || text.indexOf(query) !== -1);
      card.hidden = !ok;
      if (ok) shown += 1;
    });
    sections.forEach(function (section) {
      section.hidden = !section.querySelector(".clinic-card:not([hidden])");
    });
    if (empty) empty.hidden = shown !== 0;
    paint();
  }

  if (form) form.addEventListener("submit", function (event) { event.preventDefault(); });
  if (input) {
    input.addEventListener("input", apply);
    input.addEventListener("search", apply);
    var seen = input.value;
    setInterval(function () {
      if (input.value !== seen) {
        seen = input.value;
        apply();
      }
    }, 200);
  }
  controls.forEach(function (control) {
    control.addEventListener("click", function (event) {
      if (control.tagName === "A") event.preventDefault();
      city = control.getAttribute("data-city-filter") || "all";
      apply();
      var target = document.getElementById(city === "all" ? "directory" : city);
      if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
})();
