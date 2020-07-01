from flask import request, current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from backend.extension import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, hashed_password):
        return check_password_hash(self.password_hash, hashed_password)


class Weather:
    def __init__(self, city, date, maximum, minimum):
        self.city = city
        self.date = date
        self.max = maximum
        self.min = minimum
