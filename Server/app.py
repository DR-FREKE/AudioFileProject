import sys
import os
from flask import Flask
from dotenv import load_dotenv
from Routes.api import routehandler
from Config.config import config
from Config.database import db, mash

load_dotenv()


def create_app():
    # initialize flask here
    app = Flask(__name__)

    # setup config
    config(app)

    # init db here
    db.init_app(app)
    mash.init_app(app)

    return app


db.create_all(app=create_app())

app = create_app()

# register blueprint
app.register_blueprint(routehandler(), url_prefix="/api")

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=9001)
