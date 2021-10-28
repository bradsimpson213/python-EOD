from dotenv import load_dotenv
load_dotenv()

from app import app
from app.models import db, Joke, User

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="Brad", email="brad@gmail.com", password="password")

    joke1 = Joke(
        joke_body='What did the plumber say to the singer?',
        punchline='Nice pipes...',
        rating='G',
        user=user
    )

    joke2 = Joke(
        joke_body='What do you call a lazy doctor?',
        punchline='Dr Doo-little...',
        rating='G',
        user=user
    )

    joke3 = Joke(
        joke_body='What do you call a camel in a drought?',
        punchline='A dry humper...',
        rating='PG',
        user=user
    )
    print('DB seeded!')
    db.session.add(user)
    db.session.add(joke1)
    db.session.add(joke2)
    db.session.add(joke3)
    db.session.commit()
