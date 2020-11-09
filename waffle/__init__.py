from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc940bf3ec2d1c7abcb30ee54093ebdd' #Security Method
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waffle.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) #Database

from waffle import routes