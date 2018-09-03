from flask.cli import FlaskGroup

from project import app

cli = FlaskGroup(app)

from . import test, task_one
