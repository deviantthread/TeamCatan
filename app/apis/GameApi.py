from flask import render_template, Blueprint
from flask import request
from flask import current_app as app
import json

game_blueprint = Blueprint('game', __name__)


# this route is about interacting with the meta-data of the game. creating a new game, adding players, starting the
# game, etc

@game_blueprint.route('/game', methods=['GET'])
def index():
    return {
        "msg": "game meta here",
    }


@game_blueprint.route('/game/reset', methods=['PUT'])
def reset_game():
    app.game.reset_game()
    return '', 204


@game_blueprint.route('/game/player/<player>', methods=['PUT'])
def add_player(player):
    app.game.add_player(player)
    return '', 204
