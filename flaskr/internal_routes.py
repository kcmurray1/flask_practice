from flask import make_response, Blueprint, request

internal_bp = Blueprint("internal", __name__, url_prefix="/internal")

@internal_bp.route('/')
def internal_home():
    print(request.origin)
    return make_response({"result" : "welcome to internal!"}, 200)