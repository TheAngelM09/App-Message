from flask import Blueprint, jsonify, render_template
from src.database.redisConnect import connect

main = Blueprint('index_blueprint', __name__)

jwt = JWTManager()

jwt_redis_blocklist = connect()

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None

@main.route('/')
#@jwt_required()
def home():
    return render_template("demo.html")

