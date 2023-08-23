from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.payment_kb import payment_keyboard_kb
from loader import dp
from utils.db_api.db_commands import get_course_db


@dp.callback_query_handler(Text(startswith='row_'))
async def row_student_on_course(call: types.CallbackQuery):
    pk = call.data.split('_')[1]
    data = await get_course_db(pk)
    payment_keyboard = await payment_keyboard_kb(pk)
    await call.message.edit_text(f'''☑️ Вы выбрали курс - "{data.course_title}"
⬇️Чтобы оплатить стоимость курса в размере {data.price} рублей, нажми на кнопку ниже

ℹ️После оплаты в основном меню (/start) откроется доступ к материалу, а именно добавится новая кнопка - "📕 Обучение"


☑️Нажимая на кнопку "Оплатить", вы соглашаетесь на Политику в отношении обработки персональных данных и Публичной Офертой

<a href="https://telegra.ph/Rekvizity-08-14-2">🔘 Реквизиты</a>
<a href="https://telegra.ph/Politika-konfidencialnosti-personalnyh-dannyh-08-14">🔘 Политика в отношении обработки персональных данных</a>
<a href="https://telegra.ph/Oferta-08-14">🔘 Публичная оферта</a>''', reply_markup=payment_keyboard,
                                 disable_web_page_preview=True)


@dp.callback_query_handler(Text(startswith='pay_'))
async def go_pay(call: types.CallbackQuery):
    await call.message.delete()

    pk = call.data.split('_')[1]
    data = await get_course_db(pk)

    prices = [types.LabeledPrice(label=f'Курс "{data.course_title}"', amount=int(data.price) * 100)]

    await dp.bot.send_invoice(
        chat_id=call.from_user.id,
        title='💳 Покупка доступа к курсу',
        description='''☺️ Доступ к материалу почти в руках!''',
        start_parameter='success',
        provider_token='381764678:TEST:64010',
        currency='rub',
        prices=prices,
        payload='test'
    )


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await dp.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                           error_message="😖 Произошла внешняя ошибка, попробуйте оплатить чуть-чуть позже.")


@dp.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 2
    )

    await message.answer('''🎉 Поздравлляю!
☑️Опллата успешно прошла.

Тебе открыт доступ к новым материалам курса.
Чтобы начать заниматься, вернись в основное меню и нажми на кнопку "📕 Обучение"''')
