To create a Python virtual environment for your Flask app, follow these steps:
✅ Step 1: Create a Virtual Environment

    Open your terminal or command prompt.

    Navigate to your project directory:

cd /path/to/your/flask-app

Create the virtual environment using venv:

    python3 -m venv venv

        venv is the environment name. You can choose any name you like.

✅ Step 2: Activate the Virtual Environment

    For Linux/macOS:

source venv/bin/activate

For Windows (CMD):

venv\Scripts\activate

For Windows (PowerShell):

    .\venv\Scripts\Activate.ps1

You should see the environment name (venv) in your terminal like this:

(venv) user@machine:~/flask-app$

✅ Step 3: Install Dependencies

Make sure your requirements.txt includes the necessary packages like:

Flask
python-dotenv
Flask-SQLAlchemy
pymongo

Then install the dependencies:

pip install -r requirements.txt

✅ Step 4: Verify Environment Variables

After loading .env using dotenv in your code, check if variables are accessible:

echo $CONN_STR

If it doesn't show anything, ensure .env is correctly formatted and contains variables like:

CONN_STR=mongodb://localhost:27017
PORT=3000

✅ Step 5: Run Your App

python run.py