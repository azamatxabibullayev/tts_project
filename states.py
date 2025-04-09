from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_family = State()
    waiting_for_phone = State()
    waiting_for_pdf_choice = State()
    waiting_for_audio = State()
    waiting_for_confirmation = State()
