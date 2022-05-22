from flask import Blueprint, jsonify

hello_world_routes = Blueprint('hello_world', __name__)

@hello_world_routes.route("/")
def hello_world():
    response = {'message': 'Hello World'}
    return jsonify(response)
 