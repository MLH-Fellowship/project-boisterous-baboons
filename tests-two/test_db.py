import unittest
from peewee import *

from app import TimelinePost, get_time_line_post

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)
    
    def tearDown(self):
        test_db.drop_tables(MODELS)

        test_db.close()
    
    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content="Hello world, I'm John!")
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jame@example.com', content="Hello world, I'm Jane!")
        assert second_post.id == 2

        # Get timeline posts and assert that they are correct
        list_of_posts = list(get_time_line_post().values())
        list_one = list_of_posts[0][0]
        list_two = list_of_posts[0][1]
        
        # Check ID's
        self.assertEqual(list_one['id'], second_post.id)
        self.assertEqual(list_two['id'], first_post.id) 
        # Check Names
        self.assertEqual(list_one['name'], second_post.name)
        self.assertEqual(list_two['name'], first_post.name)
        # Check Emails
        self.assertEqual(list_one['email'], second_post.email)
        self.assertEqual(list_two['email'], first_post.email)
        # Check Content
        self.assertEqual(list_one['content'], second_post.content)
        self.assertEqual(list_two['content'], first_post.content)
        # Check Times
        self.assertEqual(list_one['created_at'], second_post.created_at)
        self.assertEqual(list_two['created_at'], first_post.created_at)
