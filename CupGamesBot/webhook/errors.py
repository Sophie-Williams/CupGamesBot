# coding: utf-8
from CupGamesBot.webhook import webhook
from CupGamesBot.database import session


@webhook.errorhandler(500)
def handle_500_error(e):
    session.rollback()
    return ''




