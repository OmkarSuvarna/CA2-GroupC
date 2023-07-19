#  reference taken from https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/08-Posts
# i.e. how to create routes, models, forms, __init__
# the code in the repository is of a blog site and we have implemented an information system for hospital
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '07e75ab07bc34c6551b87420a27584d0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from hospital import routes
from hospital import db
from hospital.models import User, Doctor, Patient, Consultation
db.create_all()
