from flask import render_template
from flask_login import current_user, login_required
from app import app


@app.route('/')
def index():
    '''Index page route'''

    return render_template('index.html.jinja')


@app.route("/profile", methods=["GET"])
@login_required
def profile():

    print(f"current user: {current_user}")
    # TODO: Query data that needs to be shown on the profile page
    return render_template('auth/profile.html.jinja',
                           user=current_user)
