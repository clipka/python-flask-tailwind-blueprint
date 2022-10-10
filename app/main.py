from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask_login import LoginManager
from .repo import memrepo
from .models import User
from .auth.use_cases import get_user


repo = memrepo.MemRepo()


app = Flask(__name__)


assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(repo, id) -> User:
    return get_user(repo, int(id))


# blueprint for auth routes
with app.app_context():
    from .auth import auth as auth_blueprint  # noqa E402
    app.register_blueprint(auth_blueprint)


@app.route('/')
def index():
    '''Index page route'''

    return render_template('index.html.jinja')
