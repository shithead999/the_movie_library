from flask import Flask
from config import Config
from models import db, User
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

from users.routes import users
from main.routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "users.login"


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    # Register Blueprints
    app.register_blueprint(users)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

