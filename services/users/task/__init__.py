from flask.cli import FlaskGroup

from project import create_app

cli = FlaskGroup(create_app=create_app)

from . import test, task_one
