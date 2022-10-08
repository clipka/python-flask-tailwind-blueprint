# python-flask-tailwind-blueprint
A blueprint of a flask based web application that uses Tailwind CSS for front end design.

## Features

### Backend

- [ ] Flask based Web application with registration and login capabilities
- [ ] Run with gunicorn
- [ ] Templates using Jinja2

### Frontend
- [ ] Tailwind CSS based frontend
- [ ] Responsive Design for mobile, tablet and big screens


### Deployment
- [ ] systemd service template



## Installation

Install virtual environment with

`python3 -m venv venv`

Activate the environment

`. venv/bin/activate`

Install required python packages

`pip install -r requirements.txt`

## Run

Start the application:

with flask (for development):

`flask --debug run --host "0.0.0.0"`

with gunicorn (for production):

`gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app`
