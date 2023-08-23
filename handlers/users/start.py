from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from filters.check_sub import check_sub_channel
from keyboards.inline.channel_keyboard import ch_kb
from keyboards.inline.main_menu_keyboard import show_menu_keyboard
from keyboards.inline.profile_keyboard import get_profile_kb
from loader import dp
from utils.db_api.db_commands import create_user, get_user, get_course_progress
from utils.misc import rate_limit


@dp.message_handler(CommandStart(), state='*')
async def start_cmd(message: types.Message, state: FSMContext):
    state_info = await state.get_state()
    if state_info == 'SupportInfo:question':
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
        return

    elif state_info == 'GitHubInfo:link':
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
        return

    user = await create_user(
        telegram_id=message.from_user.id,
        name=message.from_user.first_name,
        username=message.from_user.username
    )

    deep_link = message.get_args()
    if deep_link == '132450':
        '''
        Этот диплинк оставляем под интенсив (лидмагнит)
        '''
        pass
    elif deep_link == '32301':
        '''
        Этот диплинк под воронку
        '''
        pass
    elif deep_link == '22214':
        '''
        Этот диплинк под трипваер
        '''
        pass
    else:
        if user[1] is True:
            sub_status = await check_sub_channel(message.from_user.id)
            if sub_status:
                menu = await show_menu_keyboard(telegram_id=message.from_user.id)
                await message.answer('''📍 Добро пожаловать в основное меню!
🗺Для навигации по боту, используй кнопки, расположенные ниже

❓Есть вопрос? Введи или нажми на команду <b>/help</b>, поддержка ответит в течение 5 минут''',
                                     reply_markup=menu)
            else:
                await message.answer_sticker('CAACAgIAAxkBAAMKZMpeonFb_1MPUD_caBro6EwSu0UAAgEBAAJWnb0KIr6fDrjC5jQvBA')
                await message.answer(f'''👋Привет, {message.from_user.first_name}!

🧑‍💻Перед началом использования бота тебе необходимо <b>подписаться</b> на наш Телеграм канал''',
                                     reply_markup=ch_kb)
        else:
            sub_status = await check_sub_channel(message.from_user.id)

            if sub_status:
                menu = await show_menu_keyboard(telegram_id=message.from_user.id)
                await message.answer('''📍 Добро пожаловать в основное меню!
🗺Для навигации по боту, используй кнопки, расположенные ниже

❓Есть вопрос? Введи или нажми на команду <b>/help</b>, поддержка ответит в течение 5 минут''',
                                     reply_markup=menu)
            else:
                await message.answer_sticker('CAACAgIAAxkBAAMKZMpeonFb_1MPUD_caBro6EwSu0UAAgEBAAJWnb0KIr6fDrjC5jQvBA')
                await message.answer(f'''👋Привет, {message.from_user.first_name}!

🧑‍💻Перед началом использования бота тебе необходимо <b>подписаться</b> на наш Телеграм канал''',
                                     reply_markup=ch_kb)


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def get_sticker_file_id(message: types.Message):
    await message.answer(message.sticker.file_id)


async def get_user_profile(message: types.Message):
    profile_kb = await get_profile_kb(message.from_user.id)
    user = await get_user(message.from_user.id)
    course_progress = await get_course_progress(message.from_user.id)
    profile_photo = await dp.bot.get_user_profile_photos(message.from_user.id)
    if profile_photo['total_count'] == 0:
        await message.answer(f'''🧑‍💻<b>Имя:</b> {message.from_user.first_name} (@{message.from_user.username})
🏆<b>Уровень:</b> {user.level.level_title} {user.amount_rating}/{user.level.rating_amount}
🌐<b>GitHub</b>: {'Не привязан' if user.github_link is None else f'<a href="{user.github_link}">ссылка на гит</a>'}
📚<b>Обучается:</b> {'Нет' if user.learning is False else 'Да'}
{f'<b>Курс:</b> {course_progress.course.course_title}' if user.learning is True else ''}

<b><a href="https://telegra.ph/Kak-povysit-uroven-i-na-chto-on-vliyaet-08-03">Как повысить уровень и на что он влияет?</a></b>''',
                             reply_markup=profile_kb)
    else:
        await message.answer_photo(
            photo=profile_photo['photos'][0][-1]['file_id'],
            caption=f'''🧑‍💻<b>Имя:</b> {message.from_user.first_name} (@{message.from_user.username})
🏆<b>Уровень:</b> {user.level.level_title} {user.amount_rating}/{user.level.rating_amount}
🌐<b>GitHub</b>: {'Не привязан' if user.github_link is None else f'<a href="{user.github_link}">ссылка на гит</a>'}
📚<b>Обучается:</b> {'Нет' if user.learning is False else 'Да'}
{f'<b>Курс:</b> {course_progress.course.course_title}' if user.learning is True else ''}

<b><a href="https://telegra.ph/Kak-povysit-uroven-i-na-chto-on-vliyaet-08-03">Как повысить уровень и на что он влияет?</a></b>''',
            reply_markup=profile_kb
        )
