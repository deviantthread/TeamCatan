import time

from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

dice_log_blueprint = Blueprint('dice', __name__)


# this route is for getting the audit log

@dice_log_blueprint.route('/dice', methods=['GET'])
def get_dice():
    return {
        "lastRoll": app.game.dice.last_roll(),
        "time": time.time()
    }


@dice_log_blueprint.route('/dice/roll', methods=['GET'])
def roll_dice():
    return {
        "lastRoll": app.game.dice.roll_dice(app.game),
        "time": time.time()
    }


'''
input is expected to be in this format
{
  "player": "player_name",
  "diceRoll": 8,
  "resources": {
    "Wheat": 1,
    "Ore": 0,
    "Wood": 0,
    "Sheep": 0,
    "Brick": 0
  }
}
'''


@dice_log_blueprint.route('/dice/map', methods=['POST'])
def update_mapping():
    req_data = request.get_json(force=True)
    player_name = req_data["player"]
    dice_roll = req_data["diceRoll"]
    resources = req_data["resources"]
    print("got the stuff")
    app.game.dice.update_mapping(player_name, dice_roll, resources)
    print("updated the mapping")
    return '', 204


@dice_log_blueprint.route('/dice/map', methods=['GET'])
def get_mapping():
    return app.game.dice.resource_mapping
