import os
from flask import Blueprint

# app_setup = Blueprint('config', __name__)


def config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONNECTION')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
