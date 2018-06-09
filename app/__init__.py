import json
from flask import render_template
from flask import Response
from flask import Flask
from app.controllers.TopicController import topic
from app.controllers.ErrorController import errors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(errors)
app.register_blueprint(topic, url_prefix='/topic')
