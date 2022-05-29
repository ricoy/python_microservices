from flask import Flask
from app import routes

app = Flask(__name__)

app.register_blueprint(routes.hello_world_routes)
