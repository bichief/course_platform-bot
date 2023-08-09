from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.profile_keyboard import get_profile_kb
from loader import dp
from utils.db_api.db_commands import get_user, get_course_progress


@dp.callback_query_handler(Text(equals='profile'))
async def show_profile(call: types.CallbackQuery):
    user = await get_user(call.from_user.id)
    course_progress = await get_course_progress(call.from_user.id)
    profile_photo = await dp.bot.get_user_profile_photos(call.from_user.id)
    profile_kb = await get_profile_kb(call.from_user.id)
    if profile_photo['total_count'] == 0:
        await call.message.edit_text(f'''🧑‍💻<b>Имя:</b> {call.from_user.first_name} (@{call.from_user.username})
🏆<b>Уровень:</b> {user.level.level_title} {user.amount_rating}/{user.level.rating_amount}
🌐<b>GitHub</b>: {'Не привязан' if user.github_link is None else f'<a href="{user.github_link}">ссылка на гит</a>'}
📚<b>Обучается:</b> {'Нет' if user.learning is False else 'Да'}
{f'<b>Курс:</b> {course_progress.course.course_title}' if user.learning is True else ''}

<b><a href="https://telegra.ph/Kak-povysit-uroven-i-na-chto-on-vliyaet-08-03">Как повысить уровень и на что он влияет?</a></b>''',
                                     reply_markup=profile_kb)
    else:

        await call.message.delete()
        await call.message.answer_photo(
            photo=profile_photo['photos'][0][-1]['file_id'],
            caption=f'''🧑‍💻<b>Имя:</b> {call.from_user.first_name} (@{call.from_user.username})
🏆<b>Уровень:</b> {user.level.level_title} {user.amount_rating}/{user.level.rating_amount}
🌐<b>GitHub</b>: {'Не привязан' if user.github_link is None else f'<a href="{user.github_link}">ссылка на гит</a>'}
📚<b>Обучается:</b> {'Нет' if user.learning is False else 'Да'}
{f'<b>Курс:</b> {course_progress.course.course_title}' if user.learning is True else ''}

<b><a href="https://telegra.ph/Kak-povysit-uroven-i-na-chto-on-vliyaet-08-03">Как повысить уровень и на что он влияет?</a></b>''',
            reply_markup=profile_kb
        )
