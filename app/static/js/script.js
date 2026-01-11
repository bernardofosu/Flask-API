document.getElementById("fetchMovies").addEventListener("click", function() {
    fetch("http://127.0.0.1:5000/api/v1/movies/")
        .then(response => response.json())
        .then(data => {
            let moviesDiv = document.getElementById("movies");
            moviesDiv.innerHTML = "";

            data.data.forEach(movie => {
                let movieCard = `
                    <div class="movie-card">
                        <h2>${movie.name}</h2>
                        <p><strong>Genre:</strong> ${movie.genres.join(", ")}</p>
                        <p><strong>Director:</strong> ${movie.directors.join(", ")}</p>
                        <p><strong>Release Year:</strong> ${movie.releaseYear}</p>
                        <p><strong>Ratings:</strong> ${movie.ratings}/10</p>
                        <img src="/static/images/${movie.coverImage}" alt="${movie.name}">
                    </div>
                `;
                moviesDiv.innerHTML += movieCard;
            });
        })
        .catch(error => console.error("Error fetching movies:", error));
});
