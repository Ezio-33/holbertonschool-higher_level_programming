let updateHeaderButton = document.getElementById("update_header");
let header = document.querySelector("header");

updateHeaderButton.addEventListener("click", function () {
  header.textContent = "New Header!!!";
});
