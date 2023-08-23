from aiogram.dispatcher.filters.state import StatesGroup, State


class InvoiceInfo(StatesGroup):
    info = State()
