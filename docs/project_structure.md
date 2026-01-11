# 🚀 Build a Flask API with MongoDB

Follow this step-by-step guide to build a Flask API using MongoDB using the following project structure:
```js
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

# 📁 Best Practices for Organizing Your Flask Project

The best practice for organizing your Flask project is to keep the `templates/` and `static/` directories inside the `/app` directory rather than in the root directory. Here’s why:

### 🤔 Why It's Better to Place `templates/` and `static/` Inside the `/app` Directory:

#### 🏗️ **Encapsulation**:
- The `app/` directory is the core of your Flask application. By keeping everything related to your app (routes, controllers, templates, and static files) within this directory, you keep the project well-organized and encapsulated.
- This helps separate the concerns of your application (app logic in `/app`) and the configuration and environment settings (like `.env`, `requirements.txt`, and `run.py` in the root directory).

#### 📈 **Scalability**:
- As your application grows, it's easier to maintain and scale when everything related to the Flask app resides in the `/app` directory. It also prevents clutter in the root directory.

#### 📚 **Standard Structure**:
- Most Flask applications follow this structure, with the `templates/` and `static/` folders residing inside `/app`. It’s more in line with Flask’s typical project structure.

---

### 📂 **Recommended Project Structure**:

Here’s the updated Flask project structure with the `static/` folder at the root level and the `templates/` and `static/` inside the `/app` directory as well:

#### 🔍 **Explanation**:

- `/app/templates/`: Contains your HTML files (such as `index.html`).
- `/app/static/`: Stores static assets like images, CSS, and JavaScript used within the app.
- **Root-level `/static/`**: Another `static/` folder in the root directory to store global assets like CSS and JS files for public use. This is sometimes preferred if your app serves a frontend with separate static assets.
    - `/static/css/`: Stores global stylesheets.
    - `/static/js/`: Stores global JavaScript files.

---

### ⚖️ **Points to Consider**:
- If you decide to use both static folders (`/app/static/` and the root `/static/`), Flask will serve static files from the default folder (`/app/static/`) unless configured differently in your app.
- This structure allows for clear separation between app-related assets (`/app/static/` and `/app/templates/`) and public or shared static assets (`/static/` in the root).

### ⚙️ **Flask App Initialization**:
You can adjust the Flask app initialization accordingly if you want to use these static directories. If you want the root-level `static/` to be served, you’ll need to explicitly tell Flask about both:

```python
app = Flask(__name__, template_folder='app/templates', static_folder='static')
```

This ensures Flask knows where to find both your template files and static assets.

---

## 🔧 Project Structure Example:

```sh
FlaskAPI/
├── app/
│   ├── __init__.py
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   ├── utils/
│   ├── db.py
│   ├── templates/         # Templates inside /app
│   └── static/            # Static files inside /app
├── static/                # Moved to root level
│   ├── css/               # Subdirectory for CSS files
│   │   └── styles.css     # Example CSS file
│   └── js/                # Subdirectory for JavaScript files
│       └── script.js      # Example JS file
├── .env
├── requirements.txt
├── run.py
└── config.py (optional)
```

This structure keeps your Flask project clean, organized, and easy to scale as your app grows. 🌱
