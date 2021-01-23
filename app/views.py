from flask import render_template, Blueprint
from flask import current_app as app

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    app.game.temp_var = app.game.temp_var + 1
    return render_template('index.html')
