let apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
let listMovies = document.getElementById('list_movies');

async function fetchAndListMovies() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    const data = await response.json();

    data.results.forEach((movie) => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMoviesElement.appendChild(listItem);
    });

  } catch (error) {
    console.error('Fetch error:', error);
  }
}

fetchAndListMovies();
