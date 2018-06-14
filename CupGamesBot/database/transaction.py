# coding: utf-8
import hashlib
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

import config
from CupGamesBot.database import Base, session
from CupGamesBot.database.user import User


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    notification_type = Column(String)
    amount = Column(Float)
    currency = Column(String)
    datetime = Column(DateTime)
    unaccepted = Column(Boolean)
    hash = Column(String)
    user_id = Column(Integer)
    codepro = Column(Boolean)
    sender = Column(String)
    operation_id = Column(String)

    def verify(self):
        verification_string = self.notification_type + '&' + self.operation_id + '&' + str(self.amount) + '&' + self.currency + '&'
        verification_string += self.datetime.strftime("%Y-%m-%dT%H:%M:%SZ") + '&' + self.sender + '&' + str(self.codepro).lower() + '&'
        verification_string += config.TRANSACTION_SECRET_KEY + '&' + str(self.user_id)
        verification_string = verification_string.encode('utf-8')
        return hashlib.sha1(verification_string).hexdigest() == self.hash and not self.codepro and not self.unaccepted

    def apply(self):
        user = session.query(User).get(self.user_id)
        user.balance += self.amount
        session.add(self)
        session.add(user)
        session.commit()

    def __repr__(self):
        return '<Transaction with id {}>'.format(self.id)
