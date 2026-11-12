(function () {
  function fallback(value) {
    var field = document.createElement("textarea");
    field.value = value;
    field.setAttribute("readonly", "");
    field.style.position = "fixed";
    field.style.left = "-9999px";
    document.body.appendChild(field);
    field.select();
    document.execCommand("copy");
    field.remove();
  }

  document.addEventListener("click", function (event) {
    var button = event.target.closest("[data-copy]");
    if (!button) return;
    var value = button.getAttribute("data-copy") || "";
    var status = button.parentElement.querySelector("[data-copy-status]");
    var message = button.getAttribute("data-copied") || "복사했습니다.";
    function done() {
      if (status) status.textContent = message;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(value).then(done).catch(function () {
        fallback(value);
        done();
      });
    } else {
      fallback(value);
      done();
    }
  });
})();
