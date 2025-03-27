import os
from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# ✅ Load environment variables
load_dotenv()

# ✅ Connect to MongoDB using my-db and movies collection
CONN_STR = os.getenv("CONN_STR")
if not CONN_STR:
    raise ValueError("❗ Connection string not found in environment variables.")

client = MongoClient(CONN_STR)
db = client['my-db']
movies_collection = db['movies']

app = Flask(__name__)

class Movie:
    def __init__(self, name, description, duration, release_year, genres, directors, cover_image, actors, price, ratings=None, total_rating=0, release_date=None, created_by='Nana Kwasi'):
        self.name = name
        self.description = description
        self.duration = duration
        self.ratings = ratings
        self.total_rating = total_rating
        self.release_year = release_year
        self.release_date = release_date
        self.created_at = datetime.now()
        self.genres = genres
        self.directors = directors
        self.cover_image = cover_image
        self.actors = actors
        self.price = price
        self.created_by = created_by

    def to_dict(self):
        return self.__dict__

    @property
    def duration_in_hours(self):
        return round(self.duration / 60, 2)

# ✅ Validate JSON array data
def validate_list(value, field_name):
    if not isinstance(value, list) or not all(isinstance(i, str) for i in value):
        raise ValueError(f"{field_name} must be a list of strings.")

# ✅ Route to insert a movie
@app.route('/movies', methods=['POST'])
def insert_movie():
    try:
        movie_data = request.json
        movie = Movie(**movie_data)
        validate_list(movie.genres, 'Genres')
        validate_list(movie.directors, 'Directors')
        validate_list(movie.actors, 'Actors')
        result = movies_collection.insert_one(movie.to_dict())
        return jsonify({"message": "Movie inserted", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ✅ Route to get movie stats using aggregation
@app.route('/movies/stats', methods=['GET'])
def get_movie_stats():
    try:
        pipeline = [
            {
                "$group": {
                    "_id": "$release_year",
                    "avg_price": {"$avg": "$price"},
                    "min_price": {"$min": "$price"},
                    "max_price": {"$max": "$price"},
                    "avg_rating": {"$avg": "$ratings"},
                    "min_rating": {"$min": "$ratings"},
                    "max_rating": {"$max": "$ratings"},
                    "price_total": {"$sum": "$price"},
                    "movie_total": {"$sum": 1}
                }
            }
        ]
        stats = list(movies_collection.aggregate(pipeline))
        return jsonify(stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
