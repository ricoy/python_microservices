# camada responsavel pela configuracao, tratamento de execoes e execucao dos servicos
from flask import Blueprint, jsonify
from .services import HelloWorldService
from .models import HelloWorldModel

hello_world_routes = Blueprint("hello_world", __name__)


@hello_world_routes.route("/")
def hello_world():
    try:
        model = HelloWorldModel()
        service = HelloWorldService(model)
        response = {"message": service.get_hello_world_uppercase()}
        return jsonify(response), 200
    except Exception:
        response = {"message": "Erro ao processar a mensagem"}
        return jsonify(response), 500
