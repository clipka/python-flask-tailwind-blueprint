from flask import Flask, render_template
from flask_assets import Bundle, Environment


app = Flask(__name__)


assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()


@app.route('/')
def index():
    '''Index page route'''

    return render_template('index.html.jinja')
