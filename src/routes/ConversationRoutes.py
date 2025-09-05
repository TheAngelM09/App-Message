from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required
from src.database.redisConnect import connect
from src.database.connection import get_connection
from src.models.ConversationModel import ConversationModel
from decouple import config

main = Blueprint('conversation_blueprint', __name__)

jwt = JWTManager()

jwt_redis_blocklist = connect()

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None


@main.route('/get', methods=['GET'])
#@jwt_required()
def get_conversations():
    company = request.args.get("company")
    phone = request.args.get("phone")
    db = get_connection()
    if phone is not None:
        response = ConversationModel.get(db, company,phone)
        if response is not None:
            return jsonify(response)
        else: 
            return jsonify({"Error": "Not found phone"})
    else:
        return jsonify({"Error": "invalid phone"})