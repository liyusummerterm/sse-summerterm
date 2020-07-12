from flask import Flask
from .config import config
from .algo import algo_bp
from emd_lstm import test
import os


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'testing')

        app = Flask(__name__)
        app.config.from_object(config[config_name])
        app.register_blueprint(algo_bp)
        print(app.url_map)
        return app
