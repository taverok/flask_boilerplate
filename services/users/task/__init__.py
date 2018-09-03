from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)


@app.shell_context_processor
def ctx():
    return {'app': app, 'db': db}