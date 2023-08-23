from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def payment_keyboard_kb(pk):
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Оплатить', callback_data=f'pay_{pk}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='<< Назад', callback_data='courses')
                                        ]
                                    ])
    return keyboard
