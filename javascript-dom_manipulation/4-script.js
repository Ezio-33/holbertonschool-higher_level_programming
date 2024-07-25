let addItemButton = document.getElementById("add_item");
let myList = document.querySelector(".my_list");

addItemButton.addEventListener("click", function () {
  let newItem = document.createElement("li");
  newItem.textContent = "Item";
  myList.appendChild(newItem);
});
