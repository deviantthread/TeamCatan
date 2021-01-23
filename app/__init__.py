import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException

# instantiate extensions
from app.logic.Game import Game

login_manager = LoginManager()
db = SQLAlchemy()


def create_app(environment='development'):
    from config import config
    from .views import main_blueprint
    from .apis.State import state_blueprint
    from .apis.Game import game_blueprint
    from .apis.Player import player_blueprint
    from .apis.Store import store_blueprint
    from .apis.AuditLog import audit_log_blueprint
    from .auth.views import auth_blueprint
    from .auth.models import User, AnonymousUser

    # Instantiate app.
    app = Flask(__name__)

    # Set app config.
    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    # add our global game object
    app.game = Game()


    # TODO REMOVE THIS
    # temp init the game with two players
    app.game.start_staging()
    app.game.add_player("john")
    app.game.add_player("esther")
    app.game.start_game()
    app.game.players["john"].earn_resource("Wheat")

    # Set up extensions.
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints.
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(state_blueprint)
    app.register_blueprint(game_blueprint)
    app.register_blueprint(player_blueprint)
    app.register_blueprint(store_blueprint)
    app.register_blueprint(audit_log_blueprint)

    # Set up flask login.
    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    login_manager.anonymous_user = AnonymousUser

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template('error.html', error=exc), exc.code

    return app
