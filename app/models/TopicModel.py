import datetime

class TopicModel(object):
	# static vars
	_id = 1
	#hashtable
	topics = {}
	# list of key, vote tuple
	vote_lookup = []
	# instance method
	def __init__(self,topic):
		self.topic = topic
		self.votes = 0
		self.id = type(self)._id
		self.created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		
		type(self)._id += 1
		type(self).topics[self.id] = self

	def process(self):
		return {
			'id': self.id, 
			'topic': self.topic,
			'votes': self.votes,
			'created_at' : self.created_at
		}

	def upvote(self, count=1):
		self.votes += count
	
	def downvote(self, count=1):
		self.votes -= count

	@classmethod
	def get_topics(cls):
		return cls.topics

	@classmethod
	def set_topics(cls,data):
		cls.topics = data

	

