# coding: utf-8
import os


DEBUG = True

base_dir = os.path.abspath(os.path.dirname(__file__))
SSL_dir = os.path.join(base_dir, 'SSL')


# TG
token = os.environ.get('TG_TOKEN')


# WebHook
WEBHOOK_HOST = '178.172.210.42' if DEBUG else 'games.dmitry.cat'
WEBHOOK_PORT = '443'
WEBHOOK_IP = '0.0.0.0'

WEBHOOK_SSL_CERT = '/etc/ssl/certs/webhook_cert.pem'
WEBHOOK_SSL_PRVT = '/etc/ssl/private/webhook_pkey.pem'

WEBHOOK_URL_BASE = 'https://{}:{}'.format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = '/{}'.format(token)
