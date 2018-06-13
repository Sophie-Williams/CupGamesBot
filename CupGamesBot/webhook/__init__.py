# coding: utf-8
from flask import Flask


webhook = Flask(__name__)


from CupGamesBot.webhook import routes
