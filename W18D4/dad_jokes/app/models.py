from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Joke(db.Model):
    __tablename__ = 'jokes'
    id = db.Column(db.Integer, primary_key=True)
    joke_body = db.Column(db.String(255), nullable=False)
    punchline = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.String(50), default="G")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
   
    user = db.relationship('User', back_populates="joke")



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    joke = db.relationship('Joke', back_populates='user')


