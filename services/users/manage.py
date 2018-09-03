from project import app, db
from task import cli


@app.shell_context_processor
def ctx():
    return {'app': app, 'db': db}


if __name__ == '__main__':
    cli()

