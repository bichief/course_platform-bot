from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.db_commands import get_user


async def get_profile_kb(telegram_id):
    user = await get_user(telegram_id)

    if user.github_link is None:
        profile_kb = InlineKeyboardMarkup(row_width=3,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='🌐Привязать GitHub',
                                                                       callback_data='connect_git')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='⬅️ Назад', callback_data='go_back_profile')
                                              ]
                                          ])
        return profile_kb
    else:
        profile_kb = InlineKeyboardMarkup(row_width=3,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='🌐Обновить GitHub',
                                                                       callback_data='connect_git')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='⬅️ Назад', callback_data='go_back_profile')
                                              ]
                                          ])
        return profile_kb
