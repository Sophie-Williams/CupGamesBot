# coding: utf-8
import config
import string
import hashlib
from random import shuffle, choice, randint
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, String, PickleType, Boolean
from CupGamesBot.database import Base
from CupGamesBot.database.cup import Cup


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    bet = Column(Float, default=float(0))
    datetime = Column(DateTime, default=datetime.utcnow())
    user_id = Column(Integer, ForeignKey('user.id'))
    cups = Column(PickleType)
    cups_str = Column(String)
    salt = Column(String)
    hash = Column(String)
    user_choice = Column(Integer, default=None)
    result = Column(Float, default=None)
    finished = Column(Boolean, default=False)

    def __init_cups(self, win, loss, draw):
        cups = []
        for _ in range(win):
            cups.append(Cup.win)
        for _ in range(loss):
            cups.append(Cup.loss)
        for _ in range(draw):
            cups.append(Cup.draw)
        shuffle(cups)
        self.cups = cups

    def __init_hashes(self):
        self.cups_str = ''
        for cup in self.cups:
            self.cups_str += str(cup) + ';'
        self.salt = ''.join(choice(string.ascii_letters+string.digits) for _ in range(randint(10, 20)))
        hash_string = self.cups_str + self.salt
        self.hash = hashlib.md5(hash_string.encode('utf-8')).hexdigest()

    def __init__(self, bet, user):
        self.bet = bet
        self.datetime = datetime.utcnow()
        self.user_id = user.id
        self.__init_cups(win=config.GAME_WIN_CUPS, loss=config.GAME_LOSS_CUPS, draw=config.GAME_DRAW_CUPS)
        self.__init_hashes()

    def __repr__(self):
        return '<Game with id {}, bet {}, result {}, user_id {}'.format(self.id, self.bet, self.result, self.user_id)
