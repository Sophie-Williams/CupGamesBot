# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from CupGamesBot.database import Base, session
from CupGamesBot.database.lang import Lang
from CupGamesBot.database.state import State


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    balance = Column(Float, default=float(0))
    referral_invited = relationship("User")
    referral_parent_id = Column(Integer, ForeignKey('user.id'))
    games = relationship("Game")
    lang = Column(Enum(Lang), default=None)
    state = Column(Enum(State), default=None)

    def commit_to_db(self):
        session.add(self)
        session.commit()

    def __repr__(self):
        return '<User with id {} and username {}>'.format(self.id, self.username)
