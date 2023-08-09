from aiogram.dispatcher.filters.state import StatesGroup, State


class SupportInfo(StatesGroup):
    question = State()
    answer = State()