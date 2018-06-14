# coding: utf-8
from telebot.types import Update
from flask import request, abort

from CupGamesBot.webhook import webhook
from CupGamesBot.bot import bot
from config import token


@webhook.route('/'+token, methods=['POST'])
def webhook_for_bot():
    if request.is_json:
        data = request.data.decode('utf-8')
        update = Update.de_json(data)
        bot.process_new_updates([update])
        return ''
    abort(403)
