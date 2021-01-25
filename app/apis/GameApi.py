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
        "request method": request.method,
        "players": [app.game.players[player_name].to_private_json() for player_name in app.game.players],
        # "players": app.game.players,
        "staging": app.game.staging
    }


@game_blueprint.route('/game/create', methods=['PUT'])
def create_game():
    app.game.create_game()
    return '', 204


@game_blueprint.route('/game/start', methods=['PUT'])
def start_game():
    app.game.start_game()
    return '', 204


@game_blueprint.route('/game/player/<player>', methods=['PUT'])
def add_player(player):
    app.game.add_player(player)
    return '', 204
