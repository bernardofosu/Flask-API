from setuptools import setup, find_packages

setup(
    name='flask-app',
    version='1.0.0',
    description='Flask app for Beginners',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.2',
        'python-dotenv==1.0.1',
        'pymongo==4.6.3',
        'gunicorn==21.2.0',
        'requests==2.31.0',
        'vault-cli==2.3.2'
    ],
    entry_points={
        'console_scripts': [
            'start-app = run:app'  # Similar to "start": "nodemon server.js"
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)

# ✅ Explanation

#     requirements.txt → Lists all the necessary Python dependencies.

#     setup.py → Similar to package.json, used for defining metadata, scripts, and dependencies if the project needs packaging.

#     "start": "nodemon server.js" in Node.js becomes gunicorn run:app in Flask if you want to run it in production.

# ✅ Running the App

# Here’s how you’d run it:

# # Install dependencies
# pip install -r requirements.txt

# # Run the app (equivalent to npm start)
# python run.py

# # Or using gunicorn for production
# gunicorn run:app