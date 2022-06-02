import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

team = {'juan': {"name": "Juan Acosta", "university": "University of Toronto", "degree": "Computer Science", "years": 2, "github": "https://github.com/jpablo2002", "linkedin": "https://www.linkedin.com/in/juanp-acosta/",
                 "visited": ["Canada", "Venezuela", "Spain", "England", "Peru", "USA"], "skills": ["HTML", "CSS", "Javascript", "React", "Node.js", "MongoDB", "Python"]},
        'malik': {"name": "Malik Baker", "university": "Boston University", "degree": "Computer Science", "years": 3, "linkedin": "https://www.linkedin.com/in/malbaker/", "github": "https://www.github.com/malbaker/", "visited": ["USA", "Jamaica"], "skills": ["Java", "Python", "C", "Linux", "Git", "Bash", "HTML", "CSS", "Bash"]},
        'noah': {"name": "Noah Romo", "university": "Florida State University", "degree": "Computer Science", "years": 3, "linkedin": "https://www.linkedin.com/in/noah-romo/", "github": "https://github.com/noahromo", "visited": ["Brazil", "Mexico", "Germany", "England", "Venezuela", "Dominican Republic", "Canada"], "skills": ["Python", "Swift", "C++", "HTML", "CSS", "Javascript"]}
        }


@app.route('/')
def index():
    return render_template('home.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/member/<member>')
def member(member):
    person = team[member]
    return render_template(f'{member}.html',
                           title="MLH Fellow",
                           name=person["name"],
                           university=person["university"],
                           member=member, url=os.getenv("URL"),
                           linkedin=person["linkedin"],
                           github=person["github"],
                           degree=person["degree"],
                           years=person["years"],
                           skills=person["skills"])
