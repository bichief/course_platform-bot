from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_kb = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='📚 F.A.Q', url='https://telegra.ph/FAQ-08-03-12')
                                   ],
                                   [
                                       InlineKeyboardButton(text='📝 Задать вопрос', callback_data='support_ask')
                                   ]
                               ])

help_back = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='⬅️ Вернуться в меню', callback_data='check_sub')
                                     ]
                                 ])


async def help_support_answer(q_telegram_id):
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='🙂 Ответить',
                                                                 callback_data=f'answer_{q_telegram_id}')
                                        ]
                                    ])
    return keyboard
