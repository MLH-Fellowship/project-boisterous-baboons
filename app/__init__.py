import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

team = {'juan': {"name": "Juan Acosta",
                 "university": "University of Toronto",
                 "degree": "BS, Computer Science",
                 "years": "2021-2025", "github": "https://github.com/jpablo2002",
                 "linkedin": "https://www.linkedin.com/in/juanp-acosta/",
                 "activities": " ",
                 "visited": [("Canada", (56.13, -106.34)), ("Venezuela", (6.423, -66.58)), ("Spain", (40.46, -3.749)), ("England", (52.35, -1.17)), ("Peru", (-9.18, -75.0)), ("USA", (37.09, -95.71))],
                 "skills": ["HTML", "CSS", "Javascript", "React", "Node.js", "MongoDB", "Python"],
                 "about": " ",
                 "seal": "toronto"},
        'malik': {"name": "Malik Baker",
                  "university": "Boston University",
                  "degree": "BA, Computer Science",
                  "years": "2020-2024",
                  "linkedin": "https://www.linkedin.com/in/malbaker/",
                  "github": "https://www.github.com/malbaker/",
                  "activities": " ",
                  "visited": [("USA", (37.09, -95.71)), ("Jamaica", 18.1, -77.29)],
                  "skills": ["Java", "Python", "C", "Linux", "Git", "Bash", "HTML", "CSS", "Bash"],
                  "about": " ",
                  "seal": "boston"},
        'noah': {"name": "Noah Romo",
                 "university": "Florida State University",
                 "degree": "BA, Computer Science",
                 "years": "2020-2024",
                 "linkedin": "https://www.linkedin.com/in/noah-romo/",
                 "github": "https://github.com/noahromo",
                 "activities": "Activities: Google Developer Student Club, Beta Theta Pi, FSU Boxing",
                 "visited": [("Brazil", (-14.235, -51.925)), ("Mexico", (23.63, -102.5)), ("Germany", (51.16, 10.45)), ("England", (52.35, -1.17)), ("Venezuela", (6.423, -66.58)), ("Dominican Republic", (18.73, -70.16)), ("Canada", (56.13, -106.34))],
                 "skills": ["Python", "Swift", "C++", "HTML", "CSS", "Javascript"],
                 "about": "Rising junior at Florida State University in pursuit of a Bachelor of Arts in Computer Science as well as a minor in innovation. App development is like trying to learn chess. So many different ideas/moves to pick from. I started as a beginner. After playing a few games each day, I've developed into a pretty decent player. Soon enough I'll be a master. I'm interested in tech entrepreneurship, fintech, mobile dev, machine learning applications, and decentralized applications. \"The people who are crazy enough to think that they can change the world are the ones who do.\" - Steve Jobs", "seal": "fsu"}
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
                           activities=person["activities"],
                           skills=person["skills"],
                           about=person["about"],
                           seal=person["seal"])
