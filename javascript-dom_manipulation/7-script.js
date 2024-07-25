document.addEventListener("DOMContentLoaded", function () {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  const listMovies = document.getElementById("list_movies");

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erreur réseau : " + response.status);
      }
      return response.json();
    })
    .then((data) => {
      data.results.forEach((movie) => {
        let li = document.createElement("li");
        li.textContent = movie.title;
        listMovies.appendChild(li);
      });
    })
    .catch((error) => {
      console.error("Erreur lors de la récupération des films :", error);
      let li = document.createElement("li");
      li.textContent = "Erreur lors du chargement des films";
      listMovies.appendChild(li);
    });
});
