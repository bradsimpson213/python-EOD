from flask import Flask, render_template, redirect
from .config import Config
from data import jokes
from .joke_form import JokeForm
import random

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def home():
    joke = random.choice(jokes)
    return render_template('index.html', page="Home", joke=joke)


@app.route('/jokes')
def all_jokes():
    return render_template('alljokes.html', page="All Jokes", jokes=jokes)


@app.route('/addjoke', methods=['GET', 'POST'])
def add_joke():
    form = JokeForm()

    if form.validate_on_submit():
        total_jokes = len(jokes)+1
        new_joke = {
            'joke': form.data['joke'],
            'punchline': form.data['punchline'],
            'rating': form.data['rating']
        }
        jokes[i] = new_joke
        return redirect('/jokes')

    return render_template('jokeform.html', form=form, errors=form.errors)