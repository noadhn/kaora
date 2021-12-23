from datetime import datetime
from kaora import db, login_manager
from flask_loginmanager import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, email, phone_number, address):
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.address = address


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    collection = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, collection, category, price, is_available, img):
        self.collection = collection
        self.category = category
        self.price = price
        self.is_available = is_available
        self.img = img


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}' is up!')"
