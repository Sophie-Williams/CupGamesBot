# coding: utf-8
from telebot import types

from CupGamesBot.database.lang import Lang
from CupGamesBot.database.state import State


class Markup:
    @staticmethod
    def choose_language(button=None):
        lang = {
            Lang.ru: 'Русский',
            Lang.en: 'English'
        }
        if button is None:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
            markup.row(lang[Lang.ru], lang[Lang.en])
            return markup
        return lang[button]

    @staticmethod
    def menu(lang, text=None):
        buttons = {
            State.rules: {
                Lang.ru: 'Правила',
                Lang.en: 'Rules'
            },
            State.co: {
                Lang.ru: 'Сотрудничество',
                Lang.en: 'Cooperation'
            },
            State.deposit: {
                Lang.ru: 'Пополнить',
                Lang.en: 'Deposit'
            },
            State.withdraw: {
                Lang.ru: 'Вывести',
                Lang.en: 'Withdraw'
            },
            State.game: {
                Lang.ru: 'Сыграть',
                Lang.en: 'Game'
            },
            State.balance: {
                Lang.ru: 'Баланс',
                Lang.en: 'Balance'
            }
        }
        if text is None:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=3)
            markup.row(buttons[State.game][lang], buttons[State.balance][lang], buttons[State.deposit][lang])
            markup.row(buttons[State.rules][lang], buttons[State.co][lang], buttons[State.withdraw][lang])
            return markup
        for k, v in buttons.items():
            if v[lang] == text:
                return k
