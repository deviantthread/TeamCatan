from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

state_blueprint = Blueprint('state', __name__)


# this route is about getting the state of the game from different players perspectives.

@state_blueprint.route('/state')
def index():
    return {
        "msg": "game state here",
        "request method": request.method,
    }


