from flask import Blueprint
from flask_cors import CORS
from backend.extension import api_ext

api_bp = Blueprint('api', __name__)
api_ext.init_app(api_bp)


from . import resource
