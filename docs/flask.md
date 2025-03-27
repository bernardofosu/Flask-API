# 🏗️ Flask Project Structure

```
my-flask-app/
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── movie_controller.py
│   ├── models/
│   │   ├── movie_model.py
│   ├── routes/
│   │   ├── movie_routes.py
│   ├── utils/
│   │   ├── custom_error.py
│   │   ├── api_features.py
│   ├── config.py
├── .env
├── .gitignore
├── run.py
├── requirements.txt
```

# 🏗️ Flask Equivalent of `server.js` in Node.js

In a Flask application, the equivalent of the `server.js` setup in Node.js would typically be handled in the **`run.py`** file. Here's how it would look:

## 🐍 **run.py** *(Equivalent to `server.js`)*
```python
import os
from dotenv import load_dotenv
from app import create_app
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Create app instance
app = create_app()

# Database Connection
try:
    conn_str = os.getenv('CONN_STR')
    client = MongoClient(conn_str)
    print("✅ Database Connected")
except Exception as e:
    print(f"❗ Database connection failed: {e}")

# Start the server
port = int(os.getenv('PORT', 3000))
app.run(host='127.0.0.1', port=port)
print(f"🚀 Server has started on http://127.0.0.1:{port}")
```

## 📝 **Explanation**

### 🌿 **Environment Variables:**
- `load_dotenv()` reads from the `.env` file (like `dotenv.config()` in Node.js).
  
By default, load_dotenv() looks for a .env file in the current directory.
- However, if your .env file is located elsewhere, you can specify the path explicitly like this:
```sh
from dotenv import load_dotenv
import os
```
# Specify the path to your .env file
```sh
env_path = os.path.join('/path/to/your/env', 'config.env')
load_dotenv(dotenv_path=env_path)
```
This will result in:
```sh
/path/to/your/env/config.env
```
✅ Explanation
- dotenv_path specifies the exact location of the .env file if it's not in the current directory.
- os.path.join() is used to create the path in a cross-platform way (works on Windows, macOS, and Linux).

### 🗄️ **Database Connection:**
- `MongoClient()` from `pymongo` is used to connect to MongoDB using the `CONN_STR`.

### 🖇️ **App Import:**
- The app instance is imported from `app/__init__.py`, just like in Node.js with `const app = require('./app')`.

### 🚀 **Server Start:**
- `app.run()` works like `app.listen()` in Express.js.

## 📦 **.env Example**
Make sure your `.env` file contains the following:

```env
CONN_STR=mongodb://localhost:27017/myDatabase
PORT=3000
```

This setup ensures your **`run.py`** becomes the proper entry point for the application, similar to how **`server.js`** works in a Node.js environment. ✅

## ✅ **Flask (.env)**

In Flask, the same `.env` file format works using **`python-dotenv`**, and you access variables using `os.getenv()`:

### 🛠️ **Example .env File**
```ini
# Vault and Database Config
VAULT_ADDR=http://127.0.0.1:8200
VAULT_ROLE_ID=your-role-id
VAULT_SECRET_ID=your-secret-id
FLASK_ENV=production
PORT=3000
CONN_STR=mongodb+srv://nana:mongodb123@cluster0.zjhgb.mongodb.net/my-db?retryWrites=true&w=majority&
```

### 📝 **Note:**
- `NODE_ENV` is commonly used in **Node.js**, but for **Flask**, `FLASK_ENV` is the correct equivalent.
- `FLASK_ENV=production` is like `NODE_ENV=production`.

---

### 🧑‍💻 **Example in Flask:**
```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print(os.getenv('VAULT_ADDR'))
print(os.getenv('CONN_STR'))
```

---

## 🚩 **Key Points to Remember**

- **Node.js** uses `process.env.VARIABLE_NAME`.
- **Flask** uses `os.getenv('VARIABLE_NAME')`.
- `.env` files in both cases are not committed to version control (**.gitignore** should include `.env`).
- Ensure **`python-dotenv`** is installed for Flask using:
  ```bash
  pip install python-dotenv
  ```

Would you like further examples on connecting to **HashiCorp Vault** or **MongoDB** using these environment variables? 🚀
