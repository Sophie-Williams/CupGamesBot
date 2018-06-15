# coding: utf-8
from CupGamesBot.bot import bot, dictionary
from CupGamesBot.bot.markups import Markup
from CupGamesBot.database import session
from CupGamesBot.database.user import User
from CupGamesBot.database.state import State
from CupGamesBot.database.lang import Lang


@bot.message_handler(commands=['reset'])
def reset_DEBUG(message):
    user = session.query(User).get(message.chat.id)
    session.delete(user)
    session.commit()


@bot.message_handler(func=lambda message: session.query(User).get(message.chat.id) is None)
def register_new_user(message):
    # Register user
    user = User(id=message.chat.id, username=message.chat.username.lower(), state=State.lang)
    user.commit_to_db()
    # Select lang
    markup = Markup.choose_language()
    bot.send_message(message.chat.id, dictionary.register_new_user['lang'], reply_markup=markup)


@bot.message_handler(func=lambda message: session.query(User).get(message.chat.id).state is State.lang)
def choose_language(message):
    user = session.query(User).get(message.chat.id)
    if message.text == Markup.choose_language(button=Lang.ru):
        user.lang = Lang.ru
    elif message.text == Markup.choose_language(button=Lang.en):
        user.lang = Lang.en
    else:
        return
    user.state = State.referral
    user.commit_to_db()
    bot.send_message(message.chat.id, dictionary.register_new_user['referral'][user.lang])


@bot.message_handler(func=lambda message: session.query(User).get(message.chat.id).state is State.referral)
def referral(message):
    user = session.query(User).get(message.chat.id)
    referral_user = session.query(User).filter_by(username=message.text.lower().replace(' ', '')).first()
    if referral_user is not None:
        referral_user.referral_invited.append(user)
        referral_user.commit_to_db()
    user.state = State.menu
    markup = Markup.menu(lang=user.lang)
    bot.send_message(message.chat.id, dictionary.register_new_user['hello'][user.lang].format(message.chat.first_name), reply_markup=markup)


@bot.message_handler(func=lambda message: session.query(User).get(message.chat.id).state is State.menu)
def menu(message):
    user = session.query(User).get(message.chat.id)
    state = Markup.menu(lang=user.lang, text=message.text)
    bot.send_message(message.chat.id, str(state))
