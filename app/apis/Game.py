from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

game_blueprint = Blueprint('game', __name__)


# this route is about interacting with the meta-data of the game. creating a new game, adding players, starting the
# game, etc

@game_blueprint.route('/game')
def index():
    return {
        "msg": "game meta here",
        "request method": request.method,
        "home page views": app.game.temp_var
    }


