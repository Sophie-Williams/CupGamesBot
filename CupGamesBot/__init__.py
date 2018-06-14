# coding: utf-8
from time import sleep

import config
from CupGamesBot import database, bot, webhook


def run():
    bot.bot.remove_webhook()
    sleep(1)
    bot.bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH, certificate=open(config.WEBHOOK_SSL_CERT, 'r'))
    webhook.webhook.run(host=config.WEBHOOK_IP, port=config.WEBHOOK_PORT, ssl_context=(config.WEBHOOK_SSL_CERT, config.WEBHOOK_SSL_PRVT), debug=True)
