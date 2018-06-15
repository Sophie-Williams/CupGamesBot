# coding: utf-8
import hashlib
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean

import config
from CupGamesBot.database import Base, session
from CupGamesBot.database.user import User


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    description = Column(String)
    datetime = Column(DateTime)
    payment_id = Column(Integer)
    order_id = Column(Integer)
    hash = Column(String)
    accepted = Column(Boolean, default=False)

    def verify(self):
        verification_string = '{}:{}:{}:{}:{}'.format(
            config.TRANSACTION_SECRET_KEY,
            str(self.amount),
            str(self.payment_id),
            str(self.order_id),
            config.TRANSACTION_MERCHANT
        )
        return hashlib.md5(verification_string.encode('utf-8')).hexdigest() == self.hash

    def apply(self):
        if self.accepted:
            return
        user = session.query(User).get(self.order_id)
        user.balance += self.amount
        self.accepted = True
        session.add(self)
        session.add(user)
        session.commit()

    def __repr__(self):
        return '<Transaction with id {}>'.format(self.id)
