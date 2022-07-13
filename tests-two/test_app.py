import unittest
import os
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
        # Burger button
        assert '<div class="menu">' in html
        assert '<span>Introduction</span>' in html
        assert '<span>About & Education</span>' in html
        assert '<span>Experience</span>' in html
        assert '<span>Projects</span>' in html
        assert '<span>Tools & Technologies</span>' in html
        assert '<span>Hobbies</span>' in html
        # About
        assert '<h2>About Me</h2>' in html
        # Education
        assert '<h2>Education</h2>' in html
        # Experiences
        assert "<h2>Where I've Worked</h2>" in html
        # Projects
        assert '<div class="projects">' in html
        # Skills
        assert '<h2>My Personal Tech Stack</h2>' in html
        # Hobbies
        assert '<h2>My Hobbies</h2>' in html
        assert '<img src="../static/img/malik_hobbies.svg" style="display: block; margin:auto">' in html
    
    def test_timeline(self):
        # GET
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # POST
        response = self.client.post("/api/timeline_post", data={
            "name": "Noah Romo",
            "email": "noahromo@test.com",
            "content": "This is a test."
        })
        assert response.status_code == 200
        html = response.get_data(as_text = True)
        assert '"name": "Noah Romo"' in html  # Need to figure out how to test data in json 
        assert '"email": "noahromo@test.com"' in html
        assert '"content": "This is a test."' in html
        # GET
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        html = response.get_data(as_text = True)
        assert '"name": "Noah Romo"' in html
        assert '"email": "noahromo@test.com"' in html
        assert '"content": "This is a test."' in html
        assert len(json["timeline_posts"]) == 1
        # Timeline Page
        response = self.client.get("/timeline")
        html = response.get_data(as_text = True)
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
