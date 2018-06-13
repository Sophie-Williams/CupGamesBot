# coding: utf-8
from CupGamesBot.bot import bot


@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)
    print(message)