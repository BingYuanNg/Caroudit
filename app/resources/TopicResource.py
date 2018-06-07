from app.models.TopicModel import TopicModel
from app.resources import utils

class TopicResource:
	def getTopicList(data):
		# sort option offset limit
		offset = int(data.get('offset')) if data.get('offset') is not None else 1
		limit = int(data.get('limit')) if data.get('offset') is not None else 10
		sort = string(data.get('sort')) if data.get('sort') is not None else "-created_at"
		reverse = True if sort.startswith('-') else False
		sortable = ['votes', 'created_at']
		sort = utils.checkIfSortable(sortable, sort[1:])

		models = TopicModel.topics
		count = len(models)
		sorted_models = sorted(models.items(),  key=lambda x: getattr(x[1],sort), reverse=reverse)

		result = {
			'paging': utils.createPaginate(offset,limit,count),
			'result': [model.process() for (key,model) in sorted_models[offset - 1 : offset - 1  + limit]] 
		}

		return result 

	def getTopic(topic_id):
		utils.checkIfExist(TopicModel.topics,topic_id)
		model = TopicModel.topics[topic_id]
		
		return model.process()

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
		utils.checkIfExist(TopicModel.topics,topic_id)
		model = TopicModel.topics[topic_id]
		
		del model
		TopicModel.vote_lookup.remove(topic_id)		
		
		return True

	def getTop(data):
		pass
