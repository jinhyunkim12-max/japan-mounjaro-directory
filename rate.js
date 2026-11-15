(function () {
  var value = document.querySelector("[data-fx-value]");
  var date = document.querySelector("[data-fx-date]");
  var tab = document.querySelector(".fx-side");
  var prices = document.getElementById("prices");
  var details = prices ? prices.querySelector("details") : null;
  var base = (tab && tab.getAttribute("data-fx-base")) || "JPY";
  var unit = Number((tab && tab.getAttribute("data-fx-unit")) || (base === "CNY" ? 1 : 100));
  var estimates = document.querySelectorAll(base === "CNY" ? "[data-cny]" : "[data-jpy]");

  function openPrices() {
    if (!prices) return;
    if (details) details.open = true;
    prices.scrollIntoView({ block: "start" });
  }

  if (tab) {
    tab.addEventListener("click", function (event) {
      var href = tab.getAttribute("href") || "";
      if (href.indexOf("#prices") === -1) return;
      var url = new URL(href, location.href);
      if (url.pathname.replace(/\/$/, "") !== location.pathname.replace(/\/$/, "")) return;
      event.preventDefault();
      openPrices();
    });
  }
  if (location.hash === "#prices") openPrices();

  if (!value && !estimates.length) return;

  function won(amount) {
    return Math.round(amount).toLocaleString("ko-KR") + "원";
  }

  function show(perUnit, isoDate) {
    if (value && isFinite(unit) && unit > 0) {
      value.textContent = (perUnit * unit).toLocaleString("ko-KR", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }) + "원";
    }
    if (date && isoDate) {
      date.textContent = isoDate.replace(/-/g, ".");
    }
    estimates.forEach(function (cell) {
      var amount = Number(cell.getAttribute(base === "CNY" ? "data-cny" : "data-jpy"));
      if (amount) cell.textContent = won(amount * perUnit);
    });
  }

  fetch("https://api.frankfurter.dev/v1/latest?from=" + encodeURIComponent(base) + "&to=KRW")
    .then(function (response) {
      if (!response.ok) throw new Error("fx");
      return response.json();
    })
    .then(function (data) {
      var perUnit = Number(data.rates && data.rates.KRW);
      if (!isFinite(perUnit) || perUnit <= 0) throw new Error("fx");
      show(perUnit, data.date);
    })
    .catch(function () {
      if (value && value.textContent.indexOf("원") === -1) {
        value.textContent = "오늘 시세를 불러오지 못했습니다.";
      }
    });
})();
