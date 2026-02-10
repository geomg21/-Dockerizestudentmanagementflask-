from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)

    department = db.Column(db.String(50))   # CSE, ECE, ME
    course = db.Column(db.String(50))       # BTech, MTech
    year = db.Column(db.Integer)            # 1,2,3,4

    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))

    photo = db.Column(db.String(200))       # profile photo path
    document = db.Column(db.String(200))    # document path

    status = db.Column(db.String(20), default="Active")

