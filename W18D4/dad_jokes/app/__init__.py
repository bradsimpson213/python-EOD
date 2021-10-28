from flask import Flask, render_template, redirect

# new import statement
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
    return render_template('index.html', page="Home", joke=joke)


@app.route('/jokes')
def all_jokes():
    jokes = Joke.query.all()
    return render_template('alljokes.html', page="All Jokes", jokes=jokes)


@app.route('/addjoke', methods=['GET', 'POST'])
def add_joke():
    form = JokeForm()

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