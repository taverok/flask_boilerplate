from flask import Blueprint, jsonify

default_blueprint = Blueprint('default_routes', __name__)


@default_blueprint.route('/', methods=['GET'])
@default_blueprint.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'successss',
        'message': 'OK'
    })