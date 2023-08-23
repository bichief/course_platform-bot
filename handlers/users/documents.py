from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.document_keyboard import document_kb
from loader import dp


@dp.message_handler(Command('documents'))
async def documents_cmd(message: types.Message):
    await message.answer('🚓 Все необходимые документы расположены на клавиатуре ниже.\n'
                         'Для ознакомления с ними - нажмите на соответствующую кнопку', reply_markup=document_kb)
