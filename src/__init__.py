from flask import Flask
from flask_jwt_extended import JWTManager
from .routes import IndexRoutes

app = Flask(__name__)

jwt = JWTManager(app)

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(IndexRoutes.main, url_prefix='/')

    return app