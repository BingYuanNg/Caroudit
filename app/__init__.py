import json
from flask import Response, abort, jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/")  
def home():
	result = "Successful"  
	output = {
		'status' : 'ok',
		'result' : result,
	}
	return jsonify(output)
