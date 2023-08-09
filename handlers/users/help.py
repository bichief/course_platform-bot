from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from data.config import admins
from keyboards.inline.help_keyboard import help_kb, help_back, help_support_answer
from loader import dp
from states.support_info import SupportInfo
from utils.misc import rate_limit


@rate_limit(10)
@dp.message_handler(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAN-ZMt6DnjsE6736kdmAg0zg1rTxoUAAgIBAAJWnb0KTuJsgctA5P8vBA')
    await message.answer('''👨‍🔧Перед тем, как задать вопрос, посмотри, возможно, ответ находится внутри F.A.Q.
👇Ответы на частозадаваемые вопросы расположены по кнопке ниже

❓Чтобы задать вопрос, нажми на соответствующую кнопку''', reply_markup=help_kb)


@dp.callback_query_handler(Text(equals='support_ask'))
async def support_ask(call: types.CallbackQuery):
    await dp.bot.delete_message(
        chat_id=call.from_user.id,
        message_id=call.message.message_id - 1
    )
    await call.message.delete()
    await call.message.answer_sticker('CAACAgIAAxkBAAOAZMt8WrVFa4bZ-46OeBTd1FiJxpcAAksCAAJWnb0KYlBF0FD6cZwvBA')
    await call.message.answer('''✏️Напиши свой вопрос, а я передам его службе поддержки!
🔄 Если ты передумал, то нажми или введи команду <b>/start</b>''')
    await SupportInfo.question.set()


@dp.message_handler(state=SupportInfo.question)
async def get_question(message: types.Message, state: FSMContext):
    question = message.text
    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 2
    )
    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 1
    )

    await message.answer_sticker('CAACAgIAAxkBAAOCZMt87fTGI2gssS0ZnLYWPXSyttAAAkgCAAJWnb0KHPVy-NwpFNAvBA')
    await message.answer('''☑️ Я успешно отправил твой вопрос службе поддержки!
🕓Примерное время ожидания ответа - 5 минут.''', reply_markup=help_back)
    await state.reset_state(True)

    support_kb = await help_support_answer(message.from_user.id)
    await dp.bot.send_sticker(
        chat_id=admins[0],
        sticker='CAACAgIAAxkBAAOEZMt9kK6H9-A2dIXquiRKcyYS49gAAkkCAAJWnb0KKpcMnQhTIQ4vBA'
    )
    await dp.bot.send_message(
        chat_id=admins[0],
        text=f'''‼️ Пришел новый вопрос от {message.from_user.first_name} (@{message.from_user.username})
❔Вопрос:

{question}''', reply_markup=support_kb
    )


@dp.callback_query_handler(Text(startswith='answer_'))
async def support_answer(call: types.CallbackQuery):
    await call.message.answer('🖍Напиши ответ на вопрос')
    await SupportInfo.answer.set()

    state = dp.current_state(chat=call.from_user.id, user=call.from_user.id)
    await state.update_data(
        {
            'telegram_id': call.data.split('_')[1]
        }
    )


@dp.message_handler(state=SupportInfo.answer)
async def send_answer(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    telegram_id = data['telegram_id']

    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 4
    )

    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 3
    )

    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 2
    )

    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 1
    )
    await message.delete()

    await dp.bot.send_message(
        chat_id=telegram_id,
        text=f'''👨‍🔧 Пришел ответ от поддержки на твой вопрос!

💬Ответ поддержки:
{answer}'''
    )

    await message.answer_sticker('CAACAgIAAxkBAAOOZMuBJAFPYDlmk3vFwPn77fAMwXUAAv4AA1advQraBGEwLvnX_y8E')
    await message.answer('☑️Ответ был успешно отправлен!\n'
                         'Так держать!')
    await state.reset_state(True)
