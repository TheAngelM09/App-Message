from flask import Blueprint, jsonify

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def home():
    return jsonify('Hola Mundo')