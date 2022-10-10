# python-flask-tailwind-blueprint
A blueprint of a flask based web application that uses Tailwind CSS for front end design.

## Features

### Backend

- [ ] Flask based Web application with registration and login capabilities
- [x] Run with gunicorn
- [x] Templates using Jinja2

### Frontend
- [x] Tailwind CSS based frontend
- [ ] Responsive Design for mobile, tablet and big screens
  - [x] Navigation


### Deployment
- [ ] systemd service template


### User Management

By default, the application has an in memory database _memrepo_ with exactly one user:

- username: _"test@user.com"_
- password: _"p4ssword!"_

WARNING: You should add a preferred data base. Since _repo_ abstracts all data base accesses, it should be easy to replace the _memrepo_ with any other database.

## Installation

1. Install virtual environment with `python3 -m venv venv`
2. Activate the environment `. venv/bin/activate`
3. Install required python packages `pip install -r requirements.txt`
4. Initiate Tailwind CSS `tailwindcss init`

## Development

Each time a style in a template is changed, the following command must be run to extend the _main.css_ file

`tailwindcss -i ./app/static/src/main.css -o ./app/static/dist/main.css --minify`

## Run

Start the application:

with flask (for development):

`flask --debug run --host "0.0.0.0"`

with gunicorn (for production):

`gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app`


## Credits

Kudos to the ones described how to do things. Without you, I would not be able to create this blueprint that quick.

- Flask Tailwind Integration: https://testdriven.io/blog/flask-htmx-tailwind/
- Navigation: https://codepen.io/hulyak/pen/yLbwXvB
- Login System: https://github.com/Faruqt/Flask-Complete-Tutorial
