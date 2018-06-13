# coding: utf-8
from telebot.types import Update
from flask import request, abort

from CupGamesBot.webhook import webhook
from CupGamesBot.bot import bot
from config import token


@webhook.route('/')
def index_page():
    return 'CupGamesBot home page!'


@webhook.route('/'+token, methods=['GET', 'POST'])
def webhook_view_function():
    if request.is_json:
        data = request.data.decode('utf-8')
        update = Update.de_json(data)
        bot.process_new_updates([update])
        return ''
    abort(403)