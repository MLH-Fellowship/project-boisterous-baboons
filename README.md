# **Boisterous Baboons Portfolio Site**

This portfolio website allows users to learn more about the members of Boisterous Baboons, such as about each member's education, work experience, projects, skills, hobbies, and travel experiences.

## Our Stack

This website was built using HTML, Jinja2, CSS, and Javascript on the front-end, and the back-end was built using Python and Flask. We also used the particles.js and leaflet.js frameworks to add some of the design features.

## Getting Started

Currently you can only see the website on a local server (It is recommended to use the VSCode IDE).

The first step is to clone the repository onto your local machine:
```bash
$ git clone https://github.com/MLH-Fellowship/project-boisterous-baboons.git
```

Now follow the installation and usage steps below to render the website!

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv:
```bash
$ virtualenv env
$ source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Now check out the main branch if you aren’t already on it:
```bash
$ git checkout main
```

Create a .env file and add the variable: URL=localhost:5000

Start flask development server:
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. It will be hosted in the cloud soon so stay tuned!* 

## Troubleshooting

1. Make sure that you do not have any other environments open in the background when creating the virtual environment. This will prevent you from rendering the site. 

2. If the localhost:5000/ is in use then make sure to kill the application that is using the local server in the background or change the port to another by modifying the URL environment variable located in the .env file you created (Ex: URL=localhost:5001 instead of URL=localhost:5000)

## Contributing

Contributions to this project are [released](https://help.github.com/articles/github-terms-of-service/#6-contributions-under-repository-license) to the public under the [project's open source license](LICENSE).
