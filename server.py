from flask import Flask, request, abort
from json import loads
from push import Push
from bot import Bot
from config import *
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Repo

@app.route('/')
def hello():
    return "Hello World!"


@app.route("/", methods=['POST'])
def index():
    try:
        payload = loads(request.data)

        text = Push(payload)
        text.process()
        Bot.sendMessage(CHAT_ID, text.message)
    except:
        abort(400)

    return "Ok!"


if __name__ == "__main__":
    # This code is new     app.debug = True
    # -->
    app.run(host="0.0.0.0", port=4567)