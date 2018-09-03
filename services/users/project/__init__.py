import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.view.default import default_blueprint

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))

app.register_blueprint(default_blueprint)

db = SQLAlchemy()
db.init_app(app)

from .model import *    # noqa
