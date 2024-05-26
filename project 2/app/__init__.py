# app/__init__.py

# Import necessary modules from Flask and its extensions
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Configure the Flask application
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://anitta:attina12@localhost/restaurant'

# Initialize extensions with the Flask app
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'

# Initialize Flask-Migrate with the Flask app and SQLAlchemy db
migrate = Migrate(app, db)

# Import User model to use in the user loader function
from app.models import User

# Define user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes at the end to avoid circular imports
from app import routes
