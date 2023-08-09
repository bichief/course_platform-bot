from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.db_commands import get_user


async def show_menu_keyboard(telegram_id):
    user = await get_user(telegram_id)
    if user.learning is True:
        menu = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Мой профиль', callback_data='profile')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Приведи друга', callback_data='ref')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Курсы', callback_data='courses')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Обучение', callback_data='study')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Вебинары', callback_data='vebinars')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Обо мне', callback_data='about_me')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Перейти в чат', url='https://t.me'
                                                                                           '/+IYvchaLu0WdiZmEy')
                                        ]
                                    ])
        return menu
    else:
        menu = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Мой профиль', callback_data='profile')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Приведи друга', callback_data='ref')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Курсы', callback_data='courses')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Вебинары', callback_data='vebinars')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Обо мне', callback_data='about_me')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Перейти в чат', url='https://t.me'
                                                                                           '/+IYvchaLu0WdiZmEy')
                                        ]
                                    ])
        return menu
