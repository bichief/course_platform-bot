from aiogram import types
from aiogram.dispatcher.filters import Text

from filters.check_sub import check_sub_channel
from keyboards.inline.channel_keyboard import ch_kb
from keyboards.inline.main_menu_keyboard import show_menu_keyboard
from loader import dp


@dp.callback_query_handler(Text(equals='check_sub'))
async def check_sub_from_keyboard(call: types.CallbackQuery):
    sub_status = await check_sub_channel(call.from_user.id)
    if sub_status:
        await dp.bot.delete_message(
            chat_id=call.from_user.id,
            message_id=call.message.message_id - 1
        )
        menu = await show_menu_keyboard(telegram_id=call.from_user.id)
        await call.message.edit_text('''📍 Добро пожаловать в основное меню!
🗺Для навигации по боту, используй кнопки, расположенные ниже

❓Есть вопрос? Введи или нажми на команду <b>/help</b>, поддержка ответит в течение 5 минут''', reply_markup=menu)
    else:
        await dp.bot.delete_message(
            chat_id=call.from_user.id,
            message_id=call.message.message_id - 1
        )
        await call.message.delete()
        await call.message.answer_sticker('CAACAgIAAxkBAAMWZMphT3ySpceK2M5R2cF3Iu06zbAAAvMAA1advQpqG-vEx_qW_i8E')
        await call.message.answer('''✖️Мне кажется, ты пытаешься перехитрить систему
😭Я <b>не нашел</b> твоей подписки на канал.''', reply_markup=ch_kb)


@dp.callback_query_handler(Text(equals='go_back_profile'))
async def go_back_profile(call: types.CallbackQuery):
    await call.message.delete()
    menu = await show_menu_keyboard(telegram_id=call.from_user.id)
    await call.message.answer('''📍 Добро пожаловать в основное меню!
🗺Для навигации по боту, используй кнопки, расположенные ниже

❓Есть вопрос? Введи или нажми на команду <b>/help</b>, поддержка ответит в течение 5 минут''', reply_markup=menu)