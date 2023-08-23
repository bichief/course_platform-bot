from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.db_commands import get_courses


async def course_keyboard():
    data = await get_courses()
    keyboard = InlineKeyboardMarkup(row_width=3)
    for i in range(len(data)):
        course_title = data[i].course_title

        keyboard.add(InlineKeyboardButton(text=course_title, callback_data=f'course_{data[i].pk}'))

    keyboard.add(InlineKeyboardButton(text='Индивидуальное обучение', callback_data='individual'))
    keyboard.add(InlineKeyboardButton(text='<< Назад', callback_data='back_ref'))

    return keyboard


async def pk_course_keyboard(link, pk):
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Модули', url=link)
                                        ],
                                        [
                                            InlineKeyboardButton(text='Записаться на курс', callback_data=f'row_{pk}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='<< Назад', callback_data='courses')
                                        ]
                                    ])

    return keyboard


create_invoice_kb = InlineKeyboardMarkup(row_width=3,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Оставить заявку',
                                                                   callback_data='create_invoice')
                                          ],
                                          [
                                              InlineKeyboardButton(text='<< Назад', callback_data='courses')
                                          ]
                                      ])

back_individual = InlineKeyboardMarkup(row_width=3,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(text='Вернуться в меню', callback_data='check_sub')
                                           ]
                                       ])
