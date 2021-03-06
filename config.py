# coding: utf-8
import os


DEBUG = True

base_dir = os.path.abspath(os.path.dirname(__file__))
SSL_dir = os.path.join(base_dir, 'SSL')


# TG
token = ''


# Transactions
TRANSACTION_MERCHANT = '268422351'
TRANSACTION_SECRET_KEY = ''
TRANSACTION_PAYMENT_URL = {
    'RU': 'https://enpay.ru/payment/',
    'EN': 'https://enpay.ru/payment/en/'
}
MIN_IN_SUM = 100
MAX_IN_SUM = 1000
MIN_OUT_SUM = 1000
MAX_OUT_SUM = 1000


# Game
GAME_LOSS_CUPS = 3
GAME_WIN_CUPS = 2
GAME_DRAW_CUPS = 1


# Database
DATABASE_URI = 'sqlite:////Users/dmitry/Projects/CupGamesBot/CupGamesBot/database/main.db?check_same_thread=False' if DEBUG \
    else 'mysql://CupGamesBot:my_name_is_random_228@localhost/CupGamesBot'


# WebHook
WEBHOOK_HOST = '178.172.210.42' if DEBUG else 'games.dmitry.cat'
WEBHOOK_PORT = '443'
WEBHOOK_IP = '0.0.0.0'

WEBHOOK_SSL_CERT = '/etc/ssl/certs/webhook_cert.pem'
WEBHOOK_SSL_PRVT = '/etc/ssl/private/webhook_pkey.pem'

WEBHOOK_URL_BASE = 'https://{}:{}'.format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = '/{}'.format(token)
