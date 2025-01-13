from flask import Flask
from .api_routes import api_bp
from .internal_routes import internal_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp)
    app.register_blueprint(internal_bp)

    return app
    