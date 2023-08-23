from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

document_kb = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='Политика конфиденциальности персональных данных',
                                                                url='https://telegra.ph/Politika-konfidencialnosti'
                                                                    '-personalnyh-dannyh-08-14')
                                       ],
                                       [
                                           InlineKeyboardButton(text='Договор Оферты',
                                                                url='https://telegra.ph/Oferta-08-14')
                                       ],
                                       [
                                           InlineKeyboardButton(text='Реквизиты',
                                                                url='https://telegra.ph/Rekvizity-08-14-2')
                                       ]

                                   ])

document_kb_start = InlineKeyboardMarkup(row_width=3,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(
                                                     text='Политика конфиденциальности персональных данных',
                                                     url='https://telegra.ph/Politika-konfidencialnosti'
                                                         '-personalnyh-dannyh-08-14')
                                             ],
                                             [
                                                 InlineKeyboardButton(text='Договор Оферты',
                                                                      url='https://telegra.ph/Oferta-08-14')
                                             ],
                                             [
                                                 InlineKeyboardButton(text='✅ Ознакомился и согласен',
                                                                      callback_data='go_start')
                                             ]

                                         ])
