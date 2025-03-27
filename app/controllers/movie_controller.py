from flask import jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId  # Correct way
from app.Utils.custom_error import CustomError
from dotenv import load_dotenv  # ✅ Load dotenv
import os

# ✅ Load environment variables
load_dotenv()

class MovieController:
    def __init__(self):
        # ✅ Connect to MongoDB
        conn_str = os.getenv('CONN_STR')
        if not conn_str:
            raise ValueError("❗ Connection string not found in environment variables.")
        
        client = MongoClient(conn_str)
        db = client['my-db']
        self.movies_collection = db['movies']

    def validate_body(self, data):
        if not data.get('title') or not data.get('release_year'):
            raise CustomError("Not a valid movie object", 400)

    def get_all_movies(self):
        movies = list(self.movies_collection.find())
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        
        response = {
            "status": "success",
            "count": len(movies),  # ✅ Include count
            "data": movies
        }
        return jsonify(response), 200

    def get_highest_rated(self):
        movies = list(self.movies_collection.find().sort('ratings', -1).limit(5))
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        
        response = {
            "status": "success",
            "count": len(movies),  # ✅ Include count
            "data": movies
        }
        return jsonify(response), 200

    def get_single_movie(self, movie_id):
        movie = self.movies_collection.find_one({"_id": ObjectId(movie_id)})
        if not movie:
            raise CustomError("Movie not found", 404)
        
        movie['_id'] = str(movie['_id'])
        response = {
            "status": "success",
            "count": 1,  # ✅ Single item, count is 1
            "data": movie
        }
        return jsonify(response), 200

    def create_movie(self):
        data = request.get_json()
        self.validate_body(data)
        result = self.movies_collection.insert_one(data)
        data['_id'] = str(result.inserted_id)

        response = {
            "status": "success",
            "count": 1,  # ✅ One movie added
            "data": data
        }
        return jsonify(response), 201

    def update_movie(self, movie_id):
        data = request.get_json()
        result = self.movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": data})
        if result.matched_count == 0:
            raise CustomError("Movie not found", 404)

        response = {
            "status": "success",
            "count": 1,  # ✅ One movie updated
            "data": data
        }
        return jsonify(response), 200

    def delete_movie(self, movie_id):
        result = self.movies_collection.delete_one({"_id": ObjectId(movie_id)})
        if result.deleted_count == 0:
            raise CustomError("Movie not found", 404)

        return jsonify({"status": "success", "data": None}), 204  # ❌ No count here (204 No Content)

    def get_movies_by_genre(self, genre):
        movies = list(self.movies_collection.find({"genres": genre}))
        for movie in movies:
            movie['_id'] = str(movie['_id'])
        
        response = {
            "status": "success",
            "count": len(movies),  # ✅ Include count
            "data": movies
        }
        return jsonify(response), 200



# from flask import jsonify, request
# from pymongo import MongoClient
# from bson.objectid import ObjectId  # Correct way
# from app.Utils.custom_error import CustomError
# from dotenv import load_dotenv  # ✅ Load dotenv
# import os

# # ✅ Load environment variables
# load_dotenv()

# class MovieController:
#     def __init__(self):
#         # ✅ Connect to MongoDB
#         conn_str = os.getenv('CONN_STR')
#         if not conn_str:
#             raise ValueError("❗ Connection string not found in environment variables.")
        
#         client = MongoClient(conn_str)
#         db = client['my-db']
#         self.movies_collection = db['movies']

#     def validate_body(self, data):
#         if not data.get('title') or not data.get('release_year'):
#             raise CustomError("Not a valid movie object", 400)

#     def get_all_movies(self):
#         movies = list(self.movies_collection.find())
#         for movie in movies:
#             movie['_id'] = str(movie['_id'])
#         return jsonify({"status": "success", "data": movies}), 200

#     def get_highest_rated(self):
#         movies = list(self.movies_collection.find().sort('ratings', -1).limit(5))
#         for movie in movies:
#             movie['_id'] = str(movie['_id'])
#         return jsonify({"status": "success", "data": movies}), 200

#     def get_single_movie(self, movie_id):
#         movie = self.movies_collection.find_one({"_id": ObjectId(movie_id)})
#         if not movie:
#             raise CustomError("Movie not found", 404)
#         movie['_id'] = str(movie['_id'])
#         return jsonify({"status": "success", "data": movie}), 200

#     def create_movie(self):
#         data = request.get_json()
#         self.validate_body(data)
#         result = self.movies_collection.insert_one(data)
#         data['_id'] = str(result.inserted_id)
#         return jsonify({"status": "success", "data": data}), 201

#     def update_movie(self, movie_id):
#         data = request.get_json()
#         result = self.movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": data})
#         if result.matched_count == 0:
#             raise CustomError("Movie not found", 404)
#         return jsonify({"status": "success", "data": data}), 200

#     def delete_movie(self, movie_id):
#         result = self.movies_collection.delete_one({"_id": ObjectId(movie_id)})
#         if result.deleted_count == 0:
#             raise CustomError("Movie not found", 404)
#         return jsonify({"status": "success", "data": None}), 204

#     def get_movies_by_genre(self, genre):
#         movies = list(self.movies_collection.find({"genres": genre}))
#         for movie in movies:
#             movie['_id'] = str(movie['_id'])
#         return jsonify({"status": "success", "data": movies}), 200
