from app.models.TopicModel import TopicModel
from app.resources import utils

class TopicResource:
	def getTopicList(data):
		pass

	def getTopic(topic_id):
		pass
	def createTopic(data):
		def createTopic(data):
		topic = data.get('topic') if data.get('topic') is not None else ""
		utils.checkIfEmpty(topic)
		utils.checkIfLengthExceed(topic)
		model = TopicModel(topic)

		TopicModel.topics[model.id] = model	
		TopicModel.vote_lookup.append(model.id)
		
		return model.process()

	def upvoteTopic(topic_id):
		pass	

	def downvoteTopic(topic_id):
		pass

	def deleteTopic(topic_id):
		pass

	def getTop(data):
		pass
