import json
#from typing_extensions import assert_type
import unittest
import os
#from urllib import response
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Malik Baker</title>" in html
        # webpage contains "Malik Baker" and other key information
        assert "About Me" in html
        assert "Experience" in html
        assert "Education" in html
        assert "Hobbies" in html
        # assert "Travel" in html # didn't find the travel page in the project yet    

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0, len(json["timeline_posts"])

    def test_timeline_content(self):
        response = self.client.get("/timeline")
        html = response.get_data(as_text = True)
        # check that the form has all the correct fields
        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="content"' in html
        assert 'type="submit"' in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post('/api/timeline_post', data={
            'email': 'john@example.com',
            'content': "Hello World, I'm John!",
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello World, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
