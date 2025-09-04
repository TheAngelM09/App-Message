from flask import Flask
from flask_jwt_extended import JWTManager
from .routes import IndexRoutes, MessageRoutes, ConversationRoutes

app = Flask(__name__)

jwt = JWTManager(app)

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(MessageRoutes.main, url_prefix='/msg')
    app.register_blueprint(ConversationRoutes.main, url_prefix='/conv')

    return app