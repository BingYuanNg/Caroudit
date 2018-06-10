import sys
from flask import Blueprint, jsonify, request, Response
import json
from app.resources.TopicResource import TopicResource

topic = Blueprint('topic', __name__)

@topic.route('/',methods=['GET'] )
def getTopicList():
	data = request.args

	result = TopicResource.getTopicList(data)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')

@topic.route('/top',methods=['GET'])
def getTop():
	data = request.args
	result = TopicResource.getTop(data)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')

@topic.route('/<int:topic_id>',methods=['GET'])
def getTopic(topic_id):
	result = TopicResource.getTopic(topic_id)
	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')

@topic.route('/',methods=['POST'])
def createTopic():
	data = request.form
	result = TopicResource.createTopic(data)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')


@topic.route('/<int:topic_id>/upvote',methods=['POST'])
def upvoteTopic(topic_id):
	result = TopicResource.upvoteTopic(topic_id)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')

@topic.route('/<int:topic_id>/downvote',methods=['POST'])
def downTopic(topic_id):
	result = TopicResource.downvoteTopic(topic_id)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')
	
@topic.route('/<int:topic_id>',methods=['DELETE'])
def deleteTopic(topic_id):
	result = TopicResource.deleteTopic(topic_id)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')

