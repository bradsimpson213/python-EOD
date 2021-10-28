from app.models import db, Joke, User
# Adds a seed jokes, you can add other jokes here if you want
def seed_jokes():
    
    user1 = User.query.get(1)
    user2 = User.query.get(2)

    joke1 = Joke(
        joke_body='What did the plumber say to the singer?',
        punchline='Nice pipes...',
        rating='G',
        user=user1
    )

    joke2 = Joke(
        joke_body='What do you call a lazy doctor?',
        punchline='Dr Doo-little...',
        rating='G',
        user=user1
    )

    joke3 = Joke(
        joke_body='What do you call a camel in a drought?',
        punchline='A dry humper...',
        rating='PG',
        user=user2
    )

    db.session.add(joke1)
    db.session.add(joke2)
    db.session.add(joke3)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the jokes table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_jokes():
    db.session.execute('TRUNCATE jokes CASCADE;')
    db.session.commit()