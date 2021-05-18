from flask import Flask, redirect, request
from flask_migrate import Migrate
import random

# new seed import
from .seeds import seed_commands
from .config import Config
from .joke_form import JokeForm
from .models import db, Joke, User

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
#new seed command
app.cli.add_command(seed_commands)

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