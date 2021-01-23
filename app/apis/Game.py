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
        "players": [app.game.players[player_name].to_json() for player_name in app.game.players],
        # "players": app.game.players,
        "staging": app.game.staging
    }


@game_blueprint.route('/game', methods=['POST'])
def create_game():
    if request.form["action"].lower() == "create":
        app.game.start_staging()
    elif request.form["action"].lower() == "start":
        app.game.start_game()
    return '', 204


@game_blueprint.route('/game/player/<player>', methods=['PUT'])
def add_player(player):
    print("ran it at least {}".format(player))
    app.game.add_player(player)
    return '', 204
