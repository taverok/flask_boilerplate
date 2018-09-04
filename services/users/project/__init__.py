import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
from .model import *    # noqa


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))

    from project.view.default import default_blueprint
    app.register_blueprint(default_blueprint)

    db.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app


