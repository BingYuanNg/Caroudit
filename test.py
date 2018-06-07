import unittest
from app import app

class CarouditTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_home_status(self):
		result = {
			'status': 'ok',
			'result' : 'Successful',
		}

		response = self.app.get('/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.json, result )

	def test_topic_create(self):
		pass

	def test_topic_read(self):
		pass
	
	def test_topic_delete(self):
		pass
	
	def test_topic_update(self):
		pass

	def test_topic_sorted(self):
		pass

	def test_topic_upvote(self):
		pass

	def test_topic_downvote(self):
		pass

if __name__ == "__main__":
    unittest.main()