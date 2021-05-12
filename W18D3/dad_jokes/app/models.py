from app import db

class Joke(db.Model):
    __tablename__ = 'jokes'

    id = db.Column(db.Integer, primary_key=True)
    joke_body = db.Column(db.String(255))
    punchline = db.Column(db.String(255))
    # need to add rating select field