from flask import Blueprint, make_response

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/')
def api_home():
    return make_response(dict(result="welcome to api!"), 200)