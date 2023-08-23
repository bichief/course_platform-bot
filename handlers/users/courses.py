from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.courses_kb import course_keyboard, pk_course_keyboard, back_individual, \
    create_invoice_kb
from loader import dp
from states.invoice_info import InvoiceInfo
from utils.db_api.db_commands import get_course_db


@dp.callback_query_handler(Text(equals='courses'))
async def show_courses(call: types.CallbackQuery):
    keyboard = await course_keyboard()
    await call.message.edit_text('''📚 Выбери интересующий тебя курс.

🖇 Нажав, можно ознакомиться с описанием, модулями, а также стоимостью курса''',
                                 reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='course_'))
async def get_course(call: types.CallbackQuery):
    pk = call.data.split('_')[1]
    data = await get_course_db(pk)
    keyboard = await pk_course_keyboard(link=data.lessons_link, pk=pk)
    await call.message.edit_text(f'''👨‍🏫 <b>{data.course_title}</b>
    
📖 {data.course_description}

💸 Стоимость курса: <b>{data.price}</b> руб.''', reply_markup=keyboard)


@dp.callback_query_handler(Text(equals='individual'))
async def individual_course(call: types.CallbackQuery):
    await call.message.edit_text('''📌Для индивидуального формата обучения заполните форму по заявке:
👤 Имя, возраст
📲 Контактный номер телефона
❔ Пожелания, что необходимо подучить, что улучшить и т.д.''', reply_markup=create_invoice_kb)


@dp.callback_query_handler(Text(equals='create_invoice'))
async def create_invoice(call: types.CallbackQuery):
    await call.message.edit_text('''📁Отправьте заявку по форме:
👤 Имя, возраст
📲 Контактный номер телефона
❔ Пожелания, что необходимо подучить, что улучшить и т.д.''')
    await InvoiceInfo.info.set()


@dp.message_handler(state=InvoiceInfo.info)
async def get_invoice(message: types.Message, state: FSMContext):
    info = message.text
    await state.reset_state(True)

    await message.delete()
    await dp.bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id - 1
    )

    await dp.bot.send_message(
        chat_id=-1001800330006,
        text=f'''Пришла новая заявка на индивидуальное обучение!
------------------------------------
{info}
------------------------------------'''
    )
    await message.answer_sticker('CAACAgIAAxkBAAIC8mTaGDJHPPPhwvjuV6EX00Wpjq4uAAIFAwACVp29CuuXLDaLUDqGMAQ')
    await message.answer('Ваша заявка была успешно отправлена!', reply_markup=back_individual)
