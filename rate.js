(function () {
  var value = document.querySelector("[data-fx-value]");
  var date = document.querySelector("[data-fx-date]");
  var estimates = document.querySelectorAll("[data-jpy]");
  var tab = document.querySelector(".fx-side");
  var prices = document.getElementById("prices");
  var details = prices ? prices.querySelector("details") : null;

  function openPrices() {
    if (!prices || !details) return;
    details.open = true;
    prices.scrollIntoView({ block: "start" });
  }

  if (tab && details) {
    tab.addEventListener("click", function (event) {
      event.preventDefault();
      openPrices();
    });
  }
  if (location.hash === "#prices") openPrices();

  if (!value && !estimates.length) return;

  function won(amount) {
    return Math.round(amount).toLocaleString("ko-KR") + "원";
  }

  function show(perJpy, isoDate) {
    if (value) {
      value.textContent = (perJpy * 100).toLocaleString("ko-KR", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      }) + "원";
    }
    if (date && isoDate) {
      date.textContent = isoDate.replace(/-/g, ".");
    }
    estimates.forEach(function (cell) {
      var yen = Number(cell.getAttribute("data-jpy"));
      if (yen) cell.textContent = won(yen * perJpy);
    });
  }

  fetch("https://api.frankfurter.dev/v1/latest?from=JPY&to=KRW")
    .then(function (response) {
      if (!response.ok) throw new Error("fx");
      return response.json();
    })
    .then(function (data) {
      var perJpy = Number(data.rates && data.rates.KRW);
      if (!isFinite(perJpy) || perJpy <= 0) throw new Error("fx");
      show(perJpy, data.date);
    })
    .catch(function () {
      if (value && value.textContent.indexOf("원") === -1) {
        value.textContent = "오늘 시세를 불러오지 못했습니다.";
      }
    });
})();
