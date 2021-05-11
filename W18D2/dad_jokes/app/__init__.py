from flask import (Flask, render_template)
from data import jokes
import random

app = Flask(__name__)


@app.route('/')
def home():
    joke = random.choice(jokes)
    return render_template('index.html', page="Home", joke=joke)


@app.route('/jokes')
def all_jokes():
    return render_template('alljokes.html', page="All Jokes", jokes=jokes)