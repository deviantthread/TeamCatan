from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

player_blueprint = Blueprint('player', __name__)


# this route is about interacting with other players. sending resource cards to another player, stealing a resource
# card from another player, or playing a dev card

@player_blueprint.route('/player')
def index():
    return {
        "msg": "player here",
        "request method": request.method,
        "players": [app.game.players[player_name].to_json() for player_name in app.game.players]
    }


'''
input is expected to be in this format
{
  "playerFrom": "player_from_name",
  "playerTo": "player_to_name",
  "resources": {
    "Wheat": 1,
    "Ore": 0,
    "Wood": 0,
    "Sheep": 0,
    "Brick": 0
  }
}
'''


@player_blueprint.route('/player/sendCardsToPlayer', methods=['POST'])
def send_cards():
    req_data = request.get_json(force=True)

    player_from = app.game.get_player(req_data["playerFrom"])
    player_to = app.game.get_player(req_data["playerTo"])
    player_from.send_cards_to_player(player_to, req_data["resources"])

    return '', 204


'''
input is expected to be in this format
{
  "thief": "thief_player_name",
  "victim": "victim_player_name"
}
'''


@player_blueprint.route('/player/stealFromPlayer', methods=['POST'])
def steal_card():
    req_data = request.get_json(force=True)

    thief = app.game.get_player(req_data["thief"])
    victim = app.game.get_player(req_data["victim"])
    thief.steal_random_from_player(victim)

    return '', 204


'''
Expected to have two query params
player = player_name
devCard = dev_card to play
'''


@player_blueprint.route('/player/playDevCard', methods=['PUT'])
def play_dev_card():
    player_name = request.args.get("player")
    dev_card = request.args.get("devCard")

    player = app.game.get_player(player_name)
    player.play_dev_card(dev_card)

    return '', 204
