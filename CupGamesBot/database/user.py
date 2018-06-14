# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from CupGamesBot.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    balance = Column(Float, default=float(0))
    referral_invited = relationship("User")
    referral_parent_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<User with id {} and username {}>'.format(self.id, self.login)
