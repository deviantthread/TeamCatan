from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

state_blueprint = Blueprint('state', __name__)

# this route is about getting the state of the game from different players perspectives.

'''
response is in this format:
{
  "current_player": {
    "awards": [],
    "name": "john",
    "played_dev_cards": [],
    "resource_cards": {
      "Brick": 4,
      "Ore": 0,
      "Sheep": 0,
      "Wheat": 1,
      "Wood": 0
    },
    "unplayed_dev_cards": [],
    "victory_points": 0
  },
  "other_players": [
    {
      "awards": [ "LargestArmy" ],
      "name": "esther",
      "played_dev_cards": [],
      "resource_cards": 5,
      "victory_points": 0
    },
    {
      "name": "solon",
      "played_dev_cards": [],
      "resource_cards": 2,
      "victory_points": 0
    }
  ],
  "store": {
    "dev_cards": 5,
    "resource_cards": {
      "Brick": 9,
      "Ore": 19,
      "Sheep": 19,
      "Wheat": 17,
      "Wood": 19
    }
  }
}
'''


def _get_current_player(current_player_name):
    return app.game.get_player(current_player_name).to_private_json()


def _get_other_players(current_player_name):
    return [app.game.get_player(player).to_public_json() for player in app.game.players if player.lower() != current_player_name.lower()]


def _get_store():
    return app.game.store.to_public_json()


@state_blueprint.route('/state', methods=['GET'])
def get_state():
    current_player_name = request.args.get("player")
    app.game.get_player(current_player_name)

    res = {
        "current_player": _get_current_player(current_player_name),
        "other_players": _get_other_players(current_player_name),
        "store": _get_store()
    }

    return res, 200
