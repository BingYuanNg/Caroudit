from app.models.TopicModel import TopicModel
from app.resources.TopicResource import TopicResource
from app.resources.utils import CustomError

import unittest

class TopicResourceTestCase(unittest.TestCase):
	def assertTopicEqual(self, obj1, obj2):
		self.assertEqual(type(obj1), type(obj2))
		self.assertEqual(obj1.votes, obj2.votes)
		self.assertEqual(obj1.topic, obj2.topic)
		self.assertEqual(obj1.created_at, obj2.created_at)
		self.assertEqual(obj1.id, obj2.id)

	def setUp(self):
		data = {
			'topic' : "Testing Resource"
		}
		self.topic = TopicResource.createTopic(data)

	
	def test_create_failed(self):
		data = {
			'topic' : ''
		}
		with self.assertRaises(CustomError):
			new = TopicResource.createTopic(data)
	
	def test_create(self):
		data = {
			'topic' : "Testing create in resource"
		}
		new = TopicResource.createTopic(data)
		
		self.assertEqual(new,TopicModel.topics[new['id']].process());

	def test_upvote_failed(self):
		topic_id = -1
		with self.assertRaises(CustomError):
			result = TopicResource.upvoteTopic(topic_id)
			
	def test_downvote_failed(self):
		topic_id = -1
		with self.assertRaises(CustomError):
			result = TopicResource.downvoteTopic(topic_id)
	
	def test_upvote(self):
		topic_id = self.topic['id']
		votes = TopicModel.topics[topic_id].votes
		result = TopicResource.upvoteTopic(topic_id)

		self.assertEqual(votes+1, result['votes'])

	def test_downvote(self):
		topic_id = self.topic['id']
		votes = TopicModel.topics[topic_id].votes
		result = TopicResource.downvoteTopic(topic_id)

		self.assertEqual(votes-1, result['votes'])
			
	def test_delete_failed(self):
		topic_id = -1
		with self.assertRaises(CustomError):
			result = TopicResource.deleteTopic(topic_id)	

	def test_delete(self):
		topic_id = self.topic['id']
		result = TopicResource.deleteTopic(topic_id)
		self.assertTrue(result)

	def tearDown(self):
		pass

if __name__ == "__main__":
	unittest.main()