from .db import db


class Joke(db.Model):
    __tablename__ = 'jokes'
    id = db.Column(db.Integer, primary_key=True)
    joke_body = db.Column(db.String(255), nullable=False)
    punchline = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.String(50), default="G")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
   
    user = db.relationship('User', back_populates="joke")