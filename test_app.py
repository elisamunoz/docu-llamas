import unittest
import mongomock
from unittest import mock
# from utils import coll_difficulty
# def test_increase_votes():
#     collection = mongomock.MongoClient().db.collection
#     objects = [dict(votes=1), dict(votes=2), ...]
#     for obj in objects:
#         obj['_id'] = collection.insert_one(obj).inserted_id
#     increase_votes(collection)
#     for obj in objects:
#         stored_obj = collection.find_one({'_id': obj['_id']})
#         stored_obj['votes'] -= 1
#         assert stored_obj == obj # by comparing all fields we make sure only votes changed

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

# class  AppTest(unittest.TestCase):
#     @classmethod
#     def get_home():
#         page = request.args.get('page', default=1, type=int)
#         patterns_per_page = 6
#         skip = (page - 1) * patterns_per_page

#         all_categories = mongomock.categories.find()
#         total_patterns = mongomock.patterns.estimated_document_count()
#         total_pages = int(math.ceil(total_patterns / patterns_per_page))

#         patterns = mongomock.patterns.find().sort(
#             "_id", -1).skip(skip).limit(patterns_per_page)
#         return render_template(
#             "home.html",
#             patterns=patterns,
#             total_pages=total_pages,
#             current_page=page,
#             categories=all_categories
#             )