from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

player_blueprint = Blueprint('player', __name__)


# this route is about interacting with other players. sending a resource card to another player, stealing a resource
# card from another player, or playing a dev card

@player_blueprint.route('/player')
def index():
    return {
        "msg": "player here",
        "request method": request.method,
    }


