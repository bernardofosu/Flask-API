# app/db.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create a global MongoDB client
client = None
db = None

def init_db():
    global client, db
    try:
        conn_str = os.getenv('CONN_STR')
        if not conn_str:
            raise ValueError("❗ Connection string not found in environment variables.")
        client = MongoClient(conn_str)
        db = client['my-db']
    except Exception as e:
        raise Exception(f"Error initializing the database: {str(e)}")

def get_db():
    if db is None:
        init_db()
    return db
