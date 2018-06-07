import json
from flask import Response, abort, jsonify
from flask import Flask
from app.controllers.TopicController import topic

app = Flask(__name__)

app.register_blueprint(topic, url_prefix='/topic')