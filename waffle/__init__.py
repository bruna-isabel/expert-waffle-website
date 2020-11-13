from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc940bf3ec2d1c7abcb30ee54093ebdd' #Security Method
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waffle.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app) #Database
bcrypt = Bcrypt(app) #To hash passwords
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from waffle import routes