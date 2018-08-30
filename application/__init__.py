from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(**config_overrides):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py')
    app.config.update(config_overrides)

    from .views import default_router
    app.register_blueprint(default_router)

    return app

app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
