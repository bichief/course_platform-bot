from loader import bot


async def check_sub_channel(telegram_id):
    user_channel_status = await bot.get_chat_member(chat_id='@botd0t', user_id=telegram_id)
    if user_channel_status["status"] != 'left':
        return True
    else:
        return False
