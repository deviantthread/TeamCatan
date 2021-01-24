from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

store_blueprint = Blueprint('store', __name__)


# this route is about interacting with the store. earning/spending resource cards. buying dev cards.

@store_blueprint.route('/store')
def index():
    return {
        "msg": "store",
        "request method": request.method,
        "store": app.game.store.to_json()
    }


'''
input is expected to be in this format
{
  "player": "player_name",
  "resources": {
    "Wheat": 1,
    "Ore": 0,
    "Wood": 0,
    "Sheep": 0,
    "Brick": 0
  }
}
'''


@store_blueprint.route('/store/deposit', methods=['POST'])
def deposit():
    req_data = request.get_json(force=True)
    for resource_type in req_data["resources"]:
        for count in range(req_data["resources"][resource_type]):
            if app.game.get_player(req_data["player"]).spend_resource(resource_type):
                app.game.store.deposit(resource_type)
    return '', 204


@store_blueprint.route('/store/withdraw', methods=['POST'])
def withdraw():
    req_data = request.get_json(force=True)
    for resource_type in req_data["resources"]:
        for count in range(req_data["resources"][resource_type]):
            if app.game.store.withdraw(resource_type):
                app.game.get_player(req_data["player"]).earn_resource(resource_type)
    return '', 204


@store_blueprint.route('/store/buyDevCard', methods=['PUT'])
def buy_dev_card():
    player_name = request.args.get("player")
    card = app.game.store.pop_dev_card()
    if card:
        app.game.get_player(player_name).gain_dev_card(card)

    return '', 204
