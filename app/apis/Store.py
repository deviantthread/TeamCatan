from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

store_blueprint = Blueprint('store', __name__)


# this route is about interacting with the store. earning/spending resource cards. buying dev cards.

@store_blueprint.route('/store')
def index():
    return {
        "msg": "store here",
        "request method": request.method,
        "home page views": app.game.temp_var
    }


