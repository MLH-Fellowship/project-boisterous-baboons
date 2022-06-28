# **MLH Fellowship Portfolio Site Project**

This portfolio website serves a template for a simple portfolio site, and gives us a place to test the various Production Engineering skills we learn throughout the fellowship.

## Our Stack

This website was built using HTML, Jinja2, CSS, and Javascript on the front-end, and the back-end was built using Python and Flask. This project also utilizes a MySQL database server, which is required for testing and deployment.

## Getting Started

Currently you can only see the website on a local server (It is recommended to use the VSCode IDE).

The first step is to clone the repository onto your local machine:
```bash
$ git clone https://github.com/malbaker/flask-project.git
```

Now follow the installation and usage steps below to render the website!

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using venv. We will call our virtual environment `venv` for simplicity:
```bash
$ python -m venv venv
$ source venv/bin/activate
```
Make sure pip is on the latest available version by running the command:
```bash
$ pip install --upgrade pip
```

Now, use [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
$ pip install -r requirements.txt
```

## Usage

Now check out the main branch if you aren’t already on it:
```bash
$ git checkout main
```

Create a `.env` file based on `example.env` in your project root. Define the variable `URL=localhost:5000` for running the project locally. Be sure to fill out the details from your local MySQL server, or whatever platform you decide to use for a hosted DB.

Also set the variable `FLASK_ENV` to `development` for testing purposes.

Start flask development server(your python venv should be active):
```bash
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

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal.* 

## Troubleshooting

1. Make sure that you do not have any other environments open in the background when creating the virtual environment. This will prevent you from rendering the site. 

2. If the localhost:5000/ is in use then make sure to kill the application that is using the local server in the background or change the port to another by modifying the URL environment variable located in the .env file you created (Ex: URL=localhost:5001 instead of URL=localhost:5000)

## Contributing

Contributions to this project are [released](https://help.github.com/articles/github-terms-of-service/#6-contributions-under-repository-license) to the public under the [project's open source license](LICENSE).
