document.addEventListener("DOMContentLoaded", function () {
  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erreur réseau : " + response.status);
      }
      return response.json();
    })
    .then((data) => {
      let helloElement = document.getElementById("hello");
      helloElement.textContent = data.hello;
    })
    .catch((error) => {
      console.error("Erreur lors de la récupération du message :", error);
      document.getElementById("hello").textContent =
        "Erreur lors du chargement";
    });
});
