# coding: utf-8
import dateutil.parser
from flask import request, abort, render_template

import config
from CupGamesBot.webhook import webhook
from CupGamesBot.database import session
from CupGamesBot.database.transaction import Transaction
from CupGamesBot.database.user import User


@webhook.route('/transaction', methods=['POST'])
def webhook_for_transactions():
    transaction = Transaction(operation_id=request.form.get('operation_id', ''),
                              amount=float(request.form.get('amount', '0')),
                              datetime=dateutil.parser.parse(request.form.get('datetime', '')),
                              hash=request.form.get('sha1_hash', ''),
                              codepro=(request.form.get('codepro', 'false') is 'true'),
                              notification_type=request.form.get('notification_type', ''),
                              sender=request.form.get('sender', ''),
                              currency=request.form.get('currency', ''),
                              user_id=int(request.form.get('label', '')),
                              unaccepted=(request.form.get('unaccepted', 'false') is 'true'))
    if not transaction.verify():
        abort(400)
    transaction.apply()
    return ''


@webhook.route('/donate')
def webhook_for_donate():
    user_id = request.args.get('id', type=int)
    if user_id is None:
        abort(400)
    amount = request.args.get('amount', default=config.MAX_IN_SUM, type=float)
    user = session.query(User).get(user_id)
    if amount > float(config.MAX_IN_SUM) or amount < float(config.MIN_IN_SUM) or user is None:
        abort(400)
    amount = round(amount*1.02, 2)
    return render_template('donate.html', user=user, amount=amount, receiver=config.YANDEX_MONEY_WALLET)
