from flask import Blueprint
from flask_cors import CORS

websocket_bp = Blueprint('websocket', __name__)

from . import event
