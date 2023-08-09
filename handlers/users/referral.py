from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.referal_keyboard import ref_kb
from loader import dp
from utils.db_api.db_commands import get_user


@dp.callback_query_handler(Text(equals='ref'))
async def show_ref(call: types.CallbackQuery):
    user = await get_user(call.from_user.id)
    keyboard = await ref_kb(call.from_user.id)
    await call.message.edit_text(f'''🙋‍♂️<b>Как работает система?</b>

💸Система приведи друга работает по следующему принципу:
Ты отправляешь ссылку, прикрепленную ниже своему другу и если он приобретает курс,<b> твой бонусный баланс пополняется на 500 рублей</b>,
которые ты можешь потратить в виде скидки на один из курсов.
🤯Так же, <b>приведенный друг прибавляет +30 очков рейтинга</b>, что позволит прокачать свой уровень быстрее остальных!

ℹ️ <b>Приведено друзей:</b> {user.amount_ref}
<b>Бонусный баланс:</b> {user.balance_ref}

👇Чтобы поделиться ботом с другом, нажми на кнопку ниже:''', reply_markup=keyboard)
