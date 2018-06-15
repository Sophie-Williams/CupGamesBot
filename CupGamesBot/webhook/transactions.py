# coding: utf-8
import dateutil.parser
from flask import request, abort, render_template

import config
from CupGamesBot.webhook import webhook
from CupGamesBot.database import session
from CupGamesBot.database.transaction import Transaction
from CupGamesBot.database.user import User


@webhook.route('/transaction/new', methods=['POST'])
def webhook_for_transactions():
    transaction = Transaction(
        amount=float(request.form.get('amount', '0')),
        description=request.form.get('description'),
        datetime=dateutil.parser.parse(request.form.get('datetime', '')),
        payment_id=int(request.form.get('payment_id', 0)),
        order_id=int(request.form.get('order_id', 0)),
        hash=request.form.get('sign', '')
    )
    if not transaction.verify():
        abort(400)
    transaction.apply()
    return ''


@webhook.route('/transaction/donate')
def webhook_for_donate():
    user_id = request.args.get('id', type=int)
    if user_id is None:
        abort(400)
    amount = request.args.get('amount', default=config.MAX_IN_SUM, type=float)
    user = session.query(User).get(user_id)
    if amount > float(config.MAX_IN_SUM) or amount < float(config.MIN_IN_SUM) or user is None:
        abort(400)
    return render_template('donate.html', user=user, amount=amount, merchant=config.TRANSACTION_MERCHANT,
                           payment_url=config.TRANSACTION_PAYMENT_URL[str(user.lang)])
