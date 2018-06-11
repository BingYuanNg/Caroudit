import sys
from flask import Blueprint, jsonify, request, Response
import json
from app.resources.TopicResource import TopicResource

topic = Blueprint('topic', __name__)

"""
@api {get} /topic/ Get Topic List
@apiName GetTopicList
@apiGroup Topic

@apiParam [Number] offset offset.
@apiParam [Number] limit limit.
@apiParam [string] sort sort-option, Ex: -votes,+created_at where - desc, + ascending
"""
@topic.route('/',methods=['GET'] )
def getTopicList():
	data = request.args

	result = TopicResource.getTopicList(data)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')


"""
@api {get} /top/ Get Top List
@apiName GetTopList
@apiGroup Topic

"""
@topic.route('/top',methods=['GET'])
def getTop():
	data = request.args
	result = TopicResource.getTop(data)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')



"""
@api {get} /topic/:id Get Topic
@apiName GetTopic
@apiGroup Topic

"""
@topic.route('/<int:topic_id>',methods=['GET'])
def getTopic(topic_id):
	result = TopicResource.getTopic(topic_id)
	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')


"""
@api {post} /topic/:id Create Topic
@apiName CreateTopic
@apiGroup Topic

@apiParam {string} topic topic

"""
@topic.route('/',methods=['POST'])
def createTopic():
	data = request.form
	result = TopicResource.createTopic(data)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')


"""
@api {post} /topic/:id/upvote Up Topic
@apiName UpvoteTopic
@apiGroup Topic

"""
@topic.route('/<int:topic_id>/upvote',methods=['POST'])
def upvoteTopic(topic_id):
	result = TopicResource.upvoteTopic(topic_id)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')


"""
@api {post} /topic/:id/downvote Down Topic
@apiName DownvoteTopic
@apiGroup Topic

"""
@topic.route('/<int:topic_id>/downvote',methods=['POST'])
def downTopic(topic_id):
	result = TopicResource.downvoteTopic(topic_id)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')


"""
@api {delete} /topic/:id/delete Delete Topic
@apiName DeleteTopic
@apiGroup Topic

"""
@topic.route('/<int:topic_id>',methods=['DELETE'])
def deleteTopic(topic_id):
	result = TopicResource.deleteTopic(topic_id)

	output = {
		'status' : 'ok',
		'data' : result
	}
	return Response(json.dumps(output), mimetype='application/json')

