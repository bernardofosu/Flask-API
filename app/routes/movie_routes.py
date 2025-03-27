from flask import Blueprint
from app.controllers.movie_controller import MovieController

# ✅ Create Blueprint
movie_bp = Blueprint('movies', __name__)

# ✅ Create Controller Instance
movie_controller = MovieController()

# ✅ Get All Movies
@movie_bp.route('/', methods=['GET'])
def get_all_movies():
    return movie_controller.get_all_movies()

# ✅ Get Highest Rated Movies
@movie_bp.route('/highest-rated', methods=['GET'])
def get_highest_rated():
    return movie_controller.get_highest_rated()

# ✅ Get Single Movie by ID
@movie_bp.route('/<string:movie_id>', methods=['GET'])
def get_single_movie(movie_id):
    return movie_controller.get_single_movie(movie_id)

# ✅ Create a New Movie
@movie_bp.route('/', methods=['POST'])
def create_movie():
    return movie_controller.create_movie()

# ✅ Update Movie
@movie_bp.route('/<string:movie_id>', methods=['PATCH'])
def update_movie(movie_id):
    return movie_controller.update_movie(movie_id)

# ✅ Delete Movie
@movie_bp.route('/<string:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    return movie_controller.delete_movie(movie_id)

# ✅ Get Movies by Genre
@movie_bp.route('/movies-by-genre/<string:genre>', methods=['GET'])
def get_movies_by_genre(genre):
    return movie_controller.get_movies_by_genre(genre)
