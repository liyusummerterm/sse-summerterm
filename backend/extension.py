from flask import request, current_app
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from flask_socketio import SocketIO

db = SQLAlchemy()
api_ext = Api()
http_auth = HTTPBasicAuth()
socketio = SocketIO(cors_allowed_origins='*', logger=True, debug=True, engineio_logger=True)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please login to access this page.'

