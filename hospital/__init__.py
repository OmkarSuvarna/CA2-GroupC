# entry point into package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from db import hospitalDB

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '07e75ab07bc34c6551b87420a27584d0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from hospital import routes

# with app.app_context():
#     db.create_all()