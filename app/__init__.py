import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

team = {'juan': {"name": "Juan Acosta", "university": "University of Toronto", "github": "https://github.com/jpablo2002", "linkedin": "https://www.linkedin.com/in/juanp-acosta/",
                 "visited": ["Canada", "Venezuela", "Spain", "England"], "skills": ["HTML", "CSS", "Javascript", "React", "Node.js", "MongoDB", "Python"]},
        'malik': {},
        'noah': {}
        }


@app.route('/')
def index():
    return render_template('home.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/member/<member>')
def member(member):
    person = team[member]
    return render_template(f'{member}.html', title="MLH Fellow", name=person["name"], university=person["university"], member=member, url=os.getenv("URL"), linkedin=person["linkedin"], github=person["github"])
