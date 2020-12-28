import { default as films } from "./films.js";


const qForm = document.querySelector(".page-search form");
const qSearchQuery = document.querySelector(".search-input");
const qSearchResults = document.querySelector(".search-results");

qForm.addEventListener("submit", function(e) {
  e.preventDefault();

  // No blank or one character input
  let input = qSearchQuery.value.trim();
  if (!input || input.length === 1) {
    return false;
  }

  // Search for the input in the film data
  let query = new RegExp(input, "i");
  films.forEach(film => {
    if (query.test(film.title)) {
      let filmYear = film.date.split("-")[0];
      let html = `<a href="films/${filmYear}/${film.id}.html">${film.title}</a>`;
      qSearchResults.insertAdjacentHTML("beforebegin", html);
    }
  });
});
