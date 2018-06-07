from flask import Blueprint

topic = Blueprint('topic', __name__)

@topic.route('/',methods=['GET'])
def getTopicList():
	return 'GET Topic Listing'

@topic.route('/',methods=['POST'])
def createTopic():
	return 'POST Topic'

@topic.route('/<id>',methods=['GET'])
def getTopic():
	return 'GET Topic Info'

@topic.route('/<id>',methods=['PUT'])
def updateTopic():
	return 'PUT Topic'
	
@topic.route('/<id>',methods=['DELETE'])
def deleteTopic():
	return 'DELETE TOPIC'
