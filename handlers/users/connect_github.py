from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.start import get_user_profile

from loader import dp
from states.github_info import GitHubInfo
from utils.db_api.db_commands import update_github


@dp.callback_query_handler(Text(equals='connect_git'))
async def connect_git(call: types.CallbackQuery):
    await call.message.answer('''🌐Отправь мне ссылку на твой GitHub

❗️Если передумал, отправь или нажми на <b>/start</b>''')
    await GitHubInfo.link.set()


@dp.message_handler(state=GitHubInfo.link)
async def get_link(message: types.Message, state: FSMContext):
    link = message.text
    await update_github(
        telegram_id=message.from_user.id,
        link=link
    )
    await state.reset_state(True)

    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 2
    )
    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 1
    )
    await message.delete()
    await get_user_profile(message)