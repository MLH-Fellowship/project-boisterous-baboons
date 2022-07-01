from cgi import test
from enum import Flag
from unicodedata import name
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
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello World, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello World, I\'m Jane!')
        assert second_post.id == 2

        # TODO: Get timeline posts and assert that they're correct
        post_list = list(get_time_line_post().values())

        # posts should be in reverse order:
        first_listed_post = post_list[0][0]
        assert first_listed_post['id'] == second_post.id and first_listed_post['name'] == second_post.name and first_listed_post['email'] == second_post.email and first_listed_post['created_at'] == second_post.created_at
        second_listed_post = post_list[0][1]
        assert second_listed_post['id'] == first_post.id and second_listed_post['name'] == first_post.name and second_listed_post['email'] == first_post.email and second_listed_post['created_at'] == first_post.created_at