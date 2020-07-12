from flask import Flask, Blueprint
from flask_restful import Api

algo_bp = Blueprint('algo_bp', __name__)
api_ext = Api(algo_bp)

from . import resource

