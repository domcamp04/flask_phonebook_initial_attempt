from enum import unique
from app import db
import os
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    entry_form = db.relationship('PhoneBookEntry', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    

class PhoneBookEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    phone_number = db.Column(db.String(50), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Colunm(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
