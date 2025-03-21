from flask import render_template, request, send_file

from src.status.status_actions import StatusActions

from src.util import table_record_to_json, get_dict_keyvalue_or_default
from config import flask_app, qrcode
from src.auth import auth_controller
from src.util import print_to_debug_log

def get_statuses():
    auth_controller.set_authorize_current_user()
    statuses = StatusActions.get_statuses()
    return {"statuses": [table_record_to_json(status) for status in statuses]}