# coding: utf-8
from config import token
from telebot import TeleBot


bot = TeleBot(token)


from CupGamesBot.bot import commands
