from flask import Flask
from .extension import db, http_auth, api_ext
from .api import api_bp
from .config import config
from .models import User
from .index import index_bp

import os


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    register_extensions(app)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(index_bp)
    app.config.from_object(config[config_name])
    print(app.url_map)
    return app


def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()


