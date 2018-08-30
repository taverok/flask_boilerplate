from flask import Blueprint


router = Blueprint('default_router', __name__)


@router.route('/')
def init():
    return "OK"
