import unittest
import mongomock
from unittest import mock

class AppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        # flask_pymongo.PyMongo will be replaced by a fake client
        cls.patcher = mock.patch(
            'flask_pymongo.PyMongo', lambda app: mongomock.MongoClient())
        cls.patcher.start()
        # This will instantiate Mongo, so mongomock is required before
        from app import app
        cls.app = app.test_client()
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.patcher.stop()
        
    def test_get_homepage(self):
        # mongo.db.receipts.insert_one({....}})
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
