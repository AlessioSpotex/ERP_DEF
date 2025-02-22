from flask import Blueprint

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

@api_bp.route('/test')
def test_api():
    return "API funzionante!"