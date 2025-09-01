from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required
from src.database.redisConnect import connect
from decouple import config

main = Blueprint('message_blueprint', __name__)

jwt = JWTManager()

jwt_redis_blocklist = connect()

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None

@main.route('/')
@jwt_required()
def home():
    return jsonify('Views Message')

@main.route('/ws', methods=['GET','POST'])
def msg_ws():

    if request.method == "GET":
        if request.args.get('hub.verify_token') == config('WS_TOKEN'):
            return request.args.get('hub.challenge')
        else:
            return jsonify({"status": "success"}, 200)

    if request.method == 'POST':
        data = request.json
        message = {
            'telf': data["entry"][0]["changes"][0]["value"]["messages"][0]["from"],
            'name': data["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"],
            'msj': data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"],
            'time': data["entry"][0]["changes"][0]["value"]["messages"][0]["timestamp"]
        }
        return jsonify(message)