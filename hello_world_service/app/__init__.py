from flask import Flask
from flask import Flask
from app import hello_world

app = Flask(__name__)

app.register_blueprint(hello_world.hello_world_routes)   