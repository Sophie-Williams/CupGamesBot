#!/usr/bin/python3
import sys
sys.path.insert(0, '/var/www/CupGamesBot/')

activate_this = '/var/www/CupGamesBot/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from CupGamesBot import database
from CupGamesBot import webhook
from CupGamesBot import bot

from CupGamesBot.webhook import webhook as application

import config
bot.bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH, certificate=open(config.WEBHOOK_SSL_CERT, 'r'))
