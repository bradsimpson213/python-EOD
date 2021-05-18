from flask import Flask, redirect, request
from flask_migrate import Migrate
from .config import Config
from .joke_form import JokeForm
import random

from .models import db, Joke, User

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)


@app.route('/')
def home():
    jokes = Joke.query.all()
    joke = random.choice(jokes)
    return joke.to_dict()


@app.route('/jokes')
def all_jokes():
    jokes = Joke.query.all()
    return {'jokes': [joke.to_dict() for joke in jokes]}


@app.route('/addjoke', methods=['GET', 'POST'])
def add_joke():
    data = request.json

    if form.validate_on_submit():
        new_joke = Joke(
            joke_body=form.data['joke'],
            punchline=form.data['punchline'],
            rating=form.data['rating']
        )
         
        db.session.add(new_joke)
        db.session.commit()
        return redirect('/jokes')

    return render_template('jokeform.html', form=form)