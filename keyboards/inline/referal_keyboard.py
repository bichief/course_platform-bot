from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def ref_kb(telegram_id):
    text = '''
Хочешь научиться создавать чат-ботов в Telegram? Давно хотел изучить Python?
Один из лучших курсов по созданию ботов и Python в твоем распоряжении!

🔸Более 60 уроков и 40 домашних заданий!
🔸Все на простом языке. Никаких сложных слов, специально для легкого старта!
🔸Зум-сессии два раза в неделю с разбором заданий и вопросов!
🔸Вебинары на выбранную тематику!

🤔Все еще думаешь?
💰Лучшие ученики курса получают РЕАЛЬНЫЕ заказы на чат-ботов!

❗️Регистрируйся по ссылке выше и измени свою жизнь!
'''
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='🙆‍♂️ Пригласить друга',
                                                                 url=f'https://t.me/share/url?url=t.me'
                                                                     f'/CourseDotBot?start={telegram_id}&text={text}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='<< Назад', callback_data='back_ref')
                                        ]
                                    ])
    return keyboard
