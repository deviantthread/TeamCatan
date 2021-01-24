from flask import render_template, Blueprint
from flask import request
from flask import current_app as app

audit_log_blueprint = Blueprint('audit_log', __name__)


# this route is for getting the audit log

@audit_log_blueprint.route('/auditLog', methods=['GET'])
def get_audit_log():
    return {
        "auditLog": app.game.audit_log.as_list()
    }
