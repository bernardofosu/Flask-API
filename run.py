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
    print(f"🔍 Using MongoDB Connection String: {conn_str}")  # Debugging step
except Exception as e:
    print(f"❗ Database connection failed: {e}")

# Start the server
port = int(os.getenv('PORT', 5000))
app.run(host='127.0.0.1', port=port)
print(f"🚀 Server has started on http://127.0.0.1:{port}")
