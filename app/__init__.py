from flask import Flask, jsonify, request, render_template
from .routes.movie_routes import movie_bp
from .Utils.custom_error import CustomError
from .controllers.error_handler import global_error_handler
from flask_cors import CORS
from pymongo import MongoClient
import os
import logging

def create_app():
    app = Flask(__name__)
    # app = Flask(__name__, template_folder='../templates', static_folder='../static') // if they are in root dir
    # You can configure CORS with more fine-grained control as needed:
    # CORS(app, resources={r"/api/*": {"origins": "http://example.com"}})
    # This would restrict CORS for the /api/* routes only to requests from http://example.com.
    CORS(app) 

    # ✅ Configure logging
    logging.basicConfig(level=logging.INFO)

    # ✅ Connect to MongoDB
    try:
        conn_str = os.getenv('CONN_STR', 'mongodb://localhost:27017/movies_db')
        client = MongoClient(conn_str)
        app.db = client.get_database()
        logging.info("✅ Connected to MongoDB successfully")
    except Exception as e:
        logging.error(f"❗ Failed to connect to MongoDB: {e}")
        raise e

    # ✅ Middleware to parse JSON data
    @app.before_request
    def handle_json():
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                request.get_json() # This line is where the data is being fetched
            except Exception as e:
                logging.error(f"❗ Invalid JSON: {e}")
                return jsonify({"error": "Invalid JSON"}), 400

  # ✅ Web Route (Render Web Page)
    @app.route("/")
    def index():
        return render_template("index.html")  # ✅ Now it works separately from API
    
    # ✅ Using Blueprints for routing
    app.register_blueprint(movie_bp, url_prefix='/api/v1/movies')

    # ✅ 404 Error Handler
    @app.errorhandler(404)
    def handle_404(e):
        error = CustomError(f"Cannot find {request.path} on the server", 404)
        return global_error_handler(error)

    # ✅ Global Error Handler
    app.register_error_handler(CustomError, global_error_handler)

    return app
