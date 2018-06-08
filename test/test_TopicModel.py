from app.models.TopicModel import TopicModel
from app.resources.utils import CustomError

import unittest

class TopicModelTestCase(unittest.TestCase):
	def assertTopicEqual(self, obj1, obj2):
		self.assertEqual(type(obj1), type(obj2))
		self.assertEqual(obj1.votes, obj2.votes)
		self.assertEqual(obj1.topic, obj2.topic)
		self.assertEqual(obj1.created_at, obj2.created_at)
		self.assertEqual(obj1.id, obj2.id)
		return True

	def setUp(self):
		self.model = TopicModel("Testing")

	def test_create(self):
		new = TopicModel("Testing Create")
		self.assertTopicEqual(new,TopicModel.topics[new.id])
	
	def test_upvote(self):
		new = TopicModel("Testing Upvote")
		model = TopicModel.topics[new.id]
		model.upvote(10)

		self.assertEqual(model.votes,10)
		self.assertTopicEqual(new,TopicModel.topics[new.id])
	
	def test_downvote(self):
		new = TopicModel("Testing downvote")
		model = TopicModel.topics[new.id]
		model.downvote(10)
		self.assertEqual(model.votes,-10)
		self.assertTopicEqual(new,TopicModel.topics[new.id])
		
	def tearDown(self):
		TopicModel.topics = {}
		_id = 1

if __name__ == "__main__":
	unittest.main()