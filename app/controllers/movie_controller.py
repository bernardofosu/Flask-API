from flask import jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from app.Utils.custom_error import CustomError
from app.Utils.api_features import ApiFeatures
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class MovieController:
    def __init__(self):
        try:
            # Connect to MongoDB
            conn_str = os.getenv('CONN_STR')
            if not conn_str:
                raise ValueError("❗ Connection string not found in environment variables.")
            
            client = MongoClient(conn_str)
            db = client['my-db']
            self.movies_collection = db['movies']
        except Exception as e:
            raise CustomError(f"Error connecting to the database: {str(e)}", 500)

    def validate_body(self, data):
        if not data.get('title') or not data.get('release_year'):
            raise CustomError("Not a valid movie object", 400)

    def get_all_movies(self):
        try:
            # Extract query parameters from the request
            query_params = request.args

            # Initialize ApiFeatures with the collection and query parameters
            api_features = ApiFeatures(self.movies_collection, query_params)

            # Apply filtering, sorting, pagination, and field selection
            movies = (api_features
                      .filter()
                      .sort()
                      .limit_fields()
                      .paginate()
                      .execute())

            # Convert _id to string for all movies
            for movie in movies:
                movie['_id'] = str(movie['_id'])

            response = {
                "status": "success",
                "count": len(movies),
                "data": movies
            }
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"status": "fail", "message": f"Error fetching movies: {str(e)}"}), 500

    def get_highest_rated(self):
        try:
            # Similar to get_all_movies but we apply sorting by ratings
            query_params = request.args
            api_features = ApiFeatures(self.movies_collection, query_params)

            # Apply filtering and sorting
            movies = (api_features
                      .sort()  # Sorting by ratings is part of the sort method
                      .limit_fields()
                      .paginate()
                      .execute())

            # Convert _id to string for all movies
            for movie in movies:
                movie['_id'] = str(movie['_id'])

            response = {
                "status": "success",
                "count": len(movies),
                "data": movies
            }
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"status": "fail", "message": f"Error fetching highest rated movies: {str(e)}"}), 500

    def get_single_movie(self, movie_id):
        try:
            movie = self.movies_collection.find_one({"_id": ObjectId(movie_id)})
            if not movie:
                raise CustomError("Movie not found", 404)

            movie['_id'] = str(movie['_id'])
            response = {
                "status": "success",
                "count": 1,  # Single item, count is 1
                "data": movie
            }
            return jsonify(response), 200
        except CustomError as ce:
            return jsonify({"status": "fail", "message": str(ce)}), ce.status_code
        except Exception as e:
            return jsonify({"status": "fail", "message": f"Error fetching movie: {str(e)}"}), 500

    def create_movie(self):
        try:
            data = request.get_json()
            self.validate_body(data)
            result = self.movies_collection.insert_one(data)
            data['_id'] = str(result.inserted_id)

            response = {
                "status": "success",
                "count": 1,  # One movie added
                "data": data
            }
            return jsonify(response), 201
        except Exception as e:
            return jsonify({"status": "fail", "message": f"Error creating movie: {str(e)}"}), 500

    def update_movie(self, movie_id):
        try:
            data = request.get_json()
            result = self.movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": data})
            if result.matched_count == 0:
                raise CustomError("Movie not found", 404)

            response = {
                "status": "success",
                "count": 1,  # One movie updated
                "data": data
            }
            return jsonify(response), 200
        except CustomError as ce:
            return jsonify({"status": "fail", "message": str(ce)}), ce.status_code
        except Exception as e:
            return jsonify({"status": "fail", "message": f"Error updating movie: {str(e)}"}), 500

    def delete_movie(self, movie_id):
        try:
            result = self.movies_collection.delete_one({"_id": ObjectId(movie_id)})
            if result.deleted_count == 0:
                raise CustomError("Movie not found", 404)

            return jsonify({"status": "success", "data": None}), 204  # No Content
        except CustomError as ce:
            return jsonify({"status": "fail", "message": str(ce)}), ce.status_code
        except Exception as e:
            return jsonify({"status": "fail", "message": f"Error deleting movie: {str(e)}"}), 500

    def get_movies_by_genre(self, genre):
        try:
            # Use ApiFeatures for genre-based search with query parameters
            query_params = request.args
            api_features = ApiFeatures(self.movies_collection, query_params)

            # Apply filtering (by genre) and other features
            movies = (api_features
                      .filter()
                      .sort()
                      .limit_fields()
                      .paginate()
                      .execute())

            for movie in movies:
                movie['_id'] = str(movie['_id'])

            response = {
                "status": "success",
                "count": len(movies),  # Include count
                "data": movies
            }
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"status": "fail", "message": f"Error fetching movies by genre: {str(e)}"}), 500


# from flask import jsonify, request
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# from app.Utils.custom_error import CustomError
# from app.Utils.api_features import ApiFeatures
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# class MovieController:
#     def __init__(self):
#         try:
#             # Connect to MongoDB
#             conn_str = os.getenv('CONN_STR')
#             if not conn_str:
#                 raise ValueError("❗ Connection string not found in environment variables.")
            
#             client = MongoClient(conn_str)
#             db = client['my-db']
#             self.movies_collection = db['movies']
#         except Exception as e:
#             raise CustomError(f"Error connecting to the database: {str(e)}", 500)

#     def validate_body(self, data):
#         if not data.get('title') or not data.get('release_year'):
#             raise CustomError("Not a valid movie object", 400)

#     def get_all_movies(self):
#         try:
#             movies = list(self.movies_collection.find())
#             for movie in movies:
#                 movie['_id'] = str(movie['_id'])

#             response = {
#                 "count": len(movies),  # Include count
#                 "data": movies,
#                 "status": "success"
#             }
#             return jsonify(response), 200
#         except Exception as e:
#             return jsonify({"status": "fail", "message": f"Error fetching movies: {str(e)}"}), 500

#     def get_highest_rated(self):
#         try:
#             movies = list(self.movies_collection.find().sort('ratings', -1).limit(5))
#             for movie in movies:
#                 movie['_id'] = str(movie['_id'])

#             response = {
#                 "status": "success",
#                 "count": len(movies),  # Include count
#                 "data": movies
#             }
#             return jsonify(response), 200
#         except Exception as e:
#             return jsonify({"status": "fail", "message": f"Error fetching highest rated movies: {str(e)}"}), 500

#     def get_single_movie(self, movie_id):
#         try:
#             movie = self.movies_collection.find_one({"_id": ObjectId(movie_id)})
#             if not movie:
#                 raise CustomError("Movie not found", 404)

#             movie['_id'] = str(movie['_id'])
#             response = {
#                 "status": "success",
#                 "count": 1,  # Single item, count is 1
#                 "data": movie
#             }
#             return jsonify(response), 200
#         except CustomError as ce:
#             return jsonify({"status": "fail", "message": str(ce)}), ce.status_code
#         except Exception as e:
#             return jsonify({"status": "fail", "message": f"Error fetching movie: {str(e)}"}), 500

#     def create_movie(self):
#         try:
#             data = request.get_json()
#             self.validate_body(data)
#             result = self.movies_collection.insert_one(data)
#             data['_id'] = str(result.inserted_id)

#             response = {
#                 "status": "success",
#                 "count": 1,  # One movie added
#                 "data": data
#             }
#             return jsonify(response), 201
#         except Exception as e:
#             return jsonify({"status": "fail", "message": f"Error creating movie: {str(e)}"}), 500

#     def update_movie(self, movie_id):
#         try:
#             data = request.get_json()
#             result = self.movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": data})
#             if result.matched_count == 0:
#                 raise CustomError("Movie not found", 404)

#             response = {
#                 "status": "success",
#                 "count": 1,  # One movie updated
#                 "data": data
#             }
#             return jsonify(response), 200
#         except CustomError as ce:
#             return jsonify({"status": "fail", "message": str(ce)}), ce.status_code
#         except Exception as e:
#             return jsonify({"status": "fail", "message": f"Error updating movie: {str(e)}"}), 500

#     def delete_movie(self, movie_id):
#         try:
#             result = self.movies_collection.delete_one({"_id": ObjectId(movie_id)})
#             if result.deleted_count == 0:
#                 raise CustomError("Movie not found", 404)

#             return jsonify({"status": "success", "data": None}), 204  # No Content
#         except CustomError as ce:
#             return jsonify({"status": "fail", "message": str(ce)}), ce.status_code
#         except Exception as e:
#             return jsonify({"status": "fail", "message": f"Error deleting movie: {str(e)}"}), 500

#     def get_movies_by_genre(self, genre):
#         try:
#             movies = list(self.movies_collection.find({"genres": genre}))
#             for movie in movies:
#                 movie['_id'] = str(movie['_id'])

#             response = {
#                 "status": "success",
#                 "count": len(movies),  # Include count
#                 "data": movies
#             }
#             return jsonify(response), 200
#         except Exception as e:
#             return jsonify({"status": "fail", "message": f"Error fetching movies by genre: {str(e)}"}), 500


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
        
#         response = {
#             "status": "success",
#             "count": len(movies),  # ✅ Include count
#             "data": movies
#         }
#         return jsonify(response), 200

#     def get_highest_rated(self):
#         movies = list(self.movies_collection.find().sort('ratings', -1).limit(5))
#         for movie in movies:
#             movie['_id'] = str(movie['_id'])
        
#         response = {
#             "status": "success",
#             "count": len(movies),  # ✅ Include count
#             "data": movies
#         }
#         return jsonify(response), 200

#     def get_single_movie(self, movie_id):
#         movie = self.movies_collection.find_one({"_id": ObjectId(movie_id)})
#         if not movie:
#             raise CustomError("Movie not found", 404)
        
#         movie['_id'] = str(movie['_id'])
#         response = {
#             "status": "success",
#             "count": 1,  # ✅ Single item, count is 1
#             "data": movie
#         }
#         return jsonify(response), 200

#     def create_movie(self):
#         data = request.get_json()
#         self.validate_body(data)
#         result = self.movies_collection.insert_one(data)
#         data['_id'] = str(result.inserted_id)

#         response = {
#             "status": "success",
#             "count": 1,  # ✅ One movie added
#             "data": data
#         }
#         return jsonify(response), 201

#     def update_movie(self, movie_id):
#         data = request.get_json()
#         result = self.movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": data})
#         if result.matched_count == 0:
#             raise CustomError("Movie not found", 404)

#         response = {
#             "status": "success",
#             "count": 1,  # ✅ One movie updated
#             "data": data
#         }
#         return jsonify(response), 200

#     def delete_movie(self, movie_id):
#         result = self.movies_collection.delete_one({"_id": ObjectId(movie_id)})
#         if result.deleted_count == 0:
#             raise CustomError("Movie not found", 404)

#         return jsonify({"status": "success", "data": None}), 204  # ❌ No count here (204 No Content)

#     def get_movies_by_genre(self, genre):
#         movies = list(self.movies_collection.find({"genres": genre}))
#         for movie in movies:
#             movie['_id'] = str(movie['_id'])
        
#         response = {
#             "status": "success",
#             "count": len(movies),  # ✅ Include count
#             "data": movies
#         }
#         return jsonify(response), 200



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
