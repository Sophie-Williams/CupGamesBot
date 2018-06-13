# coding: utf-8
from time import sleep

import config
from CupGamesBot.bot import bot
from CupGamesBot.webhook import webhook


def run():
    bot.remove_webhook()
    sleep(1)
    bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH, certificate=open(config.WEBHOOK_SSL_CERT, 'r'))
    print(config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH)
    webhook.run(host=config.WEBHOOK_IP, port=config.WEBHOOK_PORT, ssl_context=(config.WEBHOOK_SSL_CERT, config.WEBHOOK_SSL_PRVT), debug=True)
