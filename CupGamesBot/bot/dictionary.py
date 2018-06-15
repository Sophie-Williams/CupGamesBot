# coding: utf-8
from CupGamesBot.database.lang import Lang

register_new_user = {
    'lang': 'Выберите язык. Choose your language.',
    'hello': {
            Lang.ru: 'Доброе время суток, {}! С помощью данного бота ты можешь зарабатывать деньги, используя лишь свою интуицию.',
            Lang.en: 'Hello, {}! This bot can help you make money, only with your intuition.'
        },
    'referral': {
            Lang.ru: 'Если ты пришел сюда от друга — не стоит это скрывать. Напиши мне логин своего друга, если такой есть. ' +
                     'В противном случае напиши любой текст. (Если логин друга @CupGamesBot — напиши CupGamesBot).',
            Lang.en: 'If you came here from friend — tell me about it. Write your friend`s login, if he exists. ' +
                     'Else write any text. (If your friend`s login is @CupGamesBot — write CupGamesBot).'
        }
}