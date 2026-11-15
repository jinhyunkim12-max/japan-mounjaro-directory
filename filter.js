(function () {
  var input = document.getElementById("clinic-search");
  var cards = Array.prototype.slice.call(document.querySelectorAll(".clinic-card"));
  var sections = Array.prototype.slice.call(document.querySelectorAll(".city-section"));
  var cityControls = Array.prototype.slice.call(document.querySelectorAll("[data-city-filter]"));
  var koreanControls = Array.prototype.slice.call(document.querySelectorAll("[data-korean-filter]"));
  var stayControls = Array.prototype.slice.call(document.querySelectorAll("[data-stay-filter]"));
  var empty = document.getElementById("filter-empty");
  var form = document.querySelector(".finder");
  var city = "all";
  var korean = "all";
  var stay = "all";

  function paint(controls, attr, value) {
    controls.forEach(function (control) {
      var selected = control.getAttribute(attr) === value;
      if (control.tagName === "BUTTON") control.setAttribute("aria-pressed", selected ? "true" : "false");
      control.classList.toggle("is-on", selected);
    });
  }

  function apply() {
    var query = ((input && input.value) || "").trim().toLowerCase();
    var narrowed = query || korean !== "all" || stay !== "all";
    var shown = 0;
    cards.forEach(function (card) {
      var cityOk = city === "all" || card.getAttribute("data-city") === city;
      var koreanOk = korean === "all" || card.getAttribute("data-korean") === korean;
      var stayOk = stay === "all" || card.getAttribute("data-stay") === stay;
      var text = (card.getAttribute("data-search") || "").toLowerCase();
      var ok = cityOk && koreanOk && stayOk && (!query || text.indexOf(query) !== -1);
      card.hidden = !ok;
      if (ok) shown += 1;
    });
    sections.forEach(function (section) {
      var any = !!section.querySelector(".clinic-card:not([hidden])");
      section.hidden = !any;
      if (section.tagName === "DETAILS") {
        if (narrowed) section.open = any;
        else section.open = city !== "all" && section.id === city;
      }
    });
    if (empty) empty.hidden = shown !== 0;
    paint(cityControls, "data-city-filter", city);
    paint(koreanControls, "data-korean-filter", korean);
    paint(stayControls, "data-stay-filter", stay);
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
  cityControls.forEach(function (control) {
    control.addEventListener("click", function (event) {
      if (control.tagName === "A") event.preventDefault();
      city = control.getAttribute("data-city-filter") || "all";
      apply();
      var target = document.getElementById(city === "all" ? "directory" : city);
      if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
  koreanControls.forEach(function (control) {
    control.addEventListener("click", function () {
      korean = control.getAttribute("data-korean-filter") || "all";
      apply();
    });
  });
  stayControls.forEach(function (control) {
    control.addEventListener("click", function () {
      stay = control.getAttribute("data-stay-filter") || "all";
      apply();
    });
  });
})();
