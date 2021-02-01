from flask import Blueprint
from flask import current_app as app
from flask import request

store_blueprint = Blueprint('store', __name__)


# this route is about interacting with the store. earning/spending resource cards. buying dev cards.

@store_blueprint.route('/store')
def index():
    return {
        "msg": "store",
        "request method": request.method,
        "store": app.game.store.to_private_json()
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

    player = app.game.get_player(req_data["player"])
    resources = req_data["resources"]

    app.game.store_manager.deposit(player, resources)
    return '', 204


@store_blueprint.route('/store/withdraw', methods=['POST'])
def withdraw():
    req_data = request.get_json(force=True)
    resources = req_data["resources"]
    player = app.game.get_player(req_data["player"])

    app.game.store_manager.withdraw(player, resources)
    return '', 204


@store_blueprint.route('/store/buyDevCard', methods=['PUT'])
def buy_dev_card():
    player_name = request.args.get("player")
    player = app.game.get_player(player_name)

    app.game.store_manager.buy_dev_card(player)

    return '', 204
