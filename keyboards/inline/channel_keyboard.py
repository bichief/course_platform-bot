from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ch_kb = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='✈️ Канал', url='https://t.me/botd0t')
                                 ],
                                 [
                                     InlineKeyboardButton(text='☑️ Я подписался!', callback_data='check_sub')
                                 ]
                             ])
