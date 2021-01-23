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
    Wheat: 1,
    Ore: 0,
    Wood: 0,
    Sheep: 0,
    Brick: 0
  }
}
'''

@store_blueprint.route('/store/deposit', methods=['PUT'])
def deposit():

    for resource_type in request.form["resources"]:
        for count in range(request.form["resources"][resource_type]):
            app.game.store.deposit(resource_type)
            app.game.players
    return '', 204
