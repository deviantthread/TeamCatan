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
    for resource_type in request.form["resources"]:
        for count in range(request.form["resources"][resource_type]):
            app.game.store.deposit(resource_type)
            app.game.players[request.form["player"]].spend_resource(resource_type)
    return '', 204


@store_blueprint.route('/store/withdraw', methods=['POST'])
def withdraw():
    print("running withdraw")
    for resource_type in request.form["resources"]:
        for count in range(request.form["resources"][resource_type]):
            app.game.store.withdraw(resource_type)
            app.game.players[request.form["player"]].earn_resource(resource_type)
    return '', 204
