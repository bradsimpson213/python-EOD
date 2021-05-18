from flask import Flask, request
from flask_migrate import Migrate

# new seed import
from .seeds import seed_commands
from .config import Config

from .models import db

from .api.user_routes import user_routes
from .api.joke_routes import joke_routes

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(joke_routes, url_prefix='/api/jokes')
Migrate(app, db)
#new seed command
app.cli.add_command(seed_commands)



