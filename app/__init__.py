from flask import Flask
from flask_assets import Bundle, Environment
from flask_login import LoginManager
from .repo import memrepo
from .config import dev_config


app = Flask(__name__)
app.config.from_object(dev_config)
db = memrepo.MemRepo()
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint  # noqa E402
app.register_blueprint(auth_blueprint)


from app import routes  # noqa E402


@login_manager.user_loader
def load_user(id):
    return db.get_user_by_id(id)
