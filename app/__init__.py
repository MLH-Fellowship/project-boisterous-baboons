import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

team = {'juan': {"firstname": "Juan's",
                 "name": "Juan Acosta", 
                 "university": "University of Toronto", 
                 "degree": "BS, Computer Science", 
                 "years": "2021-2025", 
                 "github": "https://github.com/jpablo2002", 
                 "linkedin": "https://www.linkedin.com/in/juanp-acosta/", 
                 "activities": "Activities: St. Michael's College Student Union, Recognized Study Group, University of Toronto Game Design and Development Club",
                 "visited": [["Canada", [56.13, -106.34]], ["Venezuela", [6.423, -66.58]], ["Spain", [40.46, -3.749]], ["England", [52.35, -1.17]], ["Peru", [-9.18, -75.0]], ["USA", [37.09, -95.71]]], 
                 "skills": ["HTML", "CSS", "Javascript", "React", "Node.js", "MongoDB", "Python"], 
                 "about": "Hello! I am currently a rising sophomore at the University of Toronto pursuing my Bachelor's degree in Computer Science. On my own time I've been learning web development from scratch and can say that I've drastically improved in this field after various courses, projects, and a pair of hackathons squeezed in throughout the school year, which have helped me broaden my horizons to decide what to learn next. My current interests include web development, mobile devleopment, AR/VR, and machine learning. \"For me, becoming isn\'t about arriving somewhere or achieving a certain aim. I see it instead as forward motion, a means of evolving, a way to reach continuously toward a better self. The journey doesn\'t end. \" - Michelle Obama", 
                 "seal": "toronto"},
        'malik': {"firstname": "Malik's",
                  "name": "Malik Baker", 
                  "university": "Boston University", 
                  "degree": "BA, Computer Science", 
                  "years": "2020-2024", 
                  "linkedin": "https://www.linkedin.com/in/malbaker/", 
                  "github": "https://www.github.com/malbaker/", 
                  "activities": "Activities: BUILDS (BU Innovation Lab and Design Space)", 
                  "visited": [["USA", [37.09, -95.71]], ["Jamaica", [18.1, -77.29]]], 
                  "skills": ["Java", "Python", "C", "Linux", "Git", "Bash", "HTML", "CSS", "Bash"], 
                  "about": "I am currently a rising Junior at Boston University pursuing my Bachelor's degree in Computer Science. Within the scope of technology, my passions include open-source software, web development and systems engineering. Outside of that I enjoy listening to music, watching movies, playing the guitar, or tinkering with my custom-built PC or keyboard.", 
                  "seal": "boston"},
        'noah': {"firstname": "Noah's",
                 "name": "Noah Romo", 
                 "university": "Florida State University", 
                 "degree": "BA, Computer Science", 
                 "years": "2020-2024", 
                 "linkedin": "https://www.linkedin.com/in/noah-romo/", 
                 "github": "https://github.com/noahromo", 
                 "activities": "Activities: Google Developer Student Club, Beta Theta Pi, FSU Boxing", 
                 "visited": [["Brazil", [-14.235, -51.925]], ["Mexico", [23.63, -102.5]], ["Germany", [51.16, 10.45]], ["England", [52.35, -1.17]],
                             ["Venezuela", [6.423, -66.58]], ["Dominican Republic", [18.73, -70.16]], ["Canada", [56.13, -106.34]]], 
                 "skills": ["Python", "Swift", "C++", "HTML", "CSS", "Javascript"], 
                 "about": "Hello! I'm a junior at Florida State University in pursuit of a Bachelor of Arts in Computer Science and a minor in innovation. App development is like trying to learn chess. There are so many different strategies. I started out as a beginner. By now I've developed into a pretty decent player. And soon enough I'll be a master! I'm interested in tech entrepreneurship, fintech, mobile development, machine learning, and decentralized applications. Currently seeking start up partners to join me on this journey. \"The people who are crazy enough to think that they can change the world are the ones who do.\" - Steve Jobs", 
                 "seal": "fsu"}
        }





@app.route('/')
def member(member="malik"):
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
                           seal=person["seal"],
                           firstname=person["firstname"])


@app.route('/visited/<member>')
def visited(member):
    person = team[member]
    return person

