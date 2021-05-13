Notes for EOD

use database.py file to drop all tables (can use it to seed later)

add 2 lines to __init__.py:
    from flask_migrate import Migrate
    Migrate(app, db)

init command
    pipenv run flask db init

    remember to add slug info
    file_template = %%(year)d%%(month).2d%%(day).2d_%%(hour).2d%%(minute).2d%%(second).2d_%%(slug)s

migrate command
    pipenv run flask db migrate -m "create users table"

upgrade command
    pipenv run flask db upgrade

downgrade command
    pipenv run flask db downgrade

help command
    pipenv run flask db --help



JSON Stuff
import request from flask
data = request.json



