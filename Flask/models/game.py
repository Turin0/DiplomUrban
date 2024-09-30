from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    size = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    reviews = db.Column(db.String, nullable=False)
    image = db.Column(db.String(300), nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)
    reviews = db.Column(db.String, nullable=False)