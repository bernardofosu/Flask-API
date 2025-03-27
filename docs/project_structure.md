# 🚀 Build a Flask API with MongoDB

Follow this step-by-step guide to build a Flask API using MongoDB using the following project structure:
```s
FlaskAPI/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── movie_routes.py
│   ├── controllers/
│   │   ├── movie_controller.py
│   │   ├── error_handler.py
│   ├── models/
│   │   ├── movie_route.py
│   ├── utils/
│   │   ├── custom_error.py
│   │   ├── api_features.py
│   ├── db.py
│
├── templates/          # Moved to root level
│   └── index.html     # Example template
│
├── static/            # Moved to root level
│   ├── css/           # Subdirectory for CSS files
│   │   └── styles.css  # Example CSS file
│   └── js/            # Subdirectory for JavaScript files
│       └── script.js   # Example JS file
│
├── .env
├── requirements.txt
└── run.py
```
## ✅ **1. Environment Setup**

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ✅ **2. Configure Environment Variables**

Create a `.env` file for sensitive data like the database connection:

```env
CONN_STR=mongodb://localhost:27017/movies_db
PORT=3000
```

---

## ✅ **3. Initialize the App**

**File:** `app/__init__.py`

- Create the Flask app using `Flask(__name__)`
- Set up routes using Blueprints
- Configure error handling with `app.register_error_handler`
- Connect the database using `app/db.py`
- Return the app instance.

---

## ✅ **4. Database Configuration**

**File:** `app/db.py`

- Connect to MongoDB using `pymongo`.
- Manage database connections and ensure they are properly handled.

---

## ✅ **5. Models**

**File:** `app/models/movie.py`

- Define your database model (Movie) using MongoDB schema.
- Manage data validations.

---

## ✅ **6. Controllers**

- **File:** `app/controllers/movie_controller.py`
  - Handle requests (GET, POST, PUT, DELETE).
  - Interact with the database using models.

- **File:** `app/controllers/error_handler.py`
  - Handle errors globally using Flask error handlers.

---

## ✅ **7. Routes**

**File:** `app/routes/movie_routes.py`

- Register the routes using Blueprints.
- Import controller functions and map them to endpoints.

---

## ✅ **8. Utilities**

- **File:** `app/utils/custom_error.py`
  - Create a `CustomError` class to handle exceptions.

- **File:** `app/utils/api_features.py`
  - Implement query filtering, pagination, and sorting logic.

---

## ✅ **9. Entry Point**

**File:** `run.py`

- Import and run the app using:

```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ✅ **Run the App**

Once you've done these steps, you can run the app using:

```bash
python run.py
```

Your Flask API should now be up and running on `http://localhost:3000`! 🎉

