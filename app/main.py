from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    '''Index page route'''

    return '<h1>Python-Flask Tailwind CSS Blueprint</h1>'
