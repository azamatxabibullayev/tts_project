from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router
from states import Registration
from config import PDF_FILES
from keyboards import get_pdf_selection_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Assalomu alaykum! Iltimos, ismingizni kiriting:")
    await state.set_state(Registration.waiting_for_name)


@router.message(Registration.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Familiyangizni kiriting:")
    await state.set_state(Registration.waiting_for_family)


@router.message(Registration.waiting_for_family)
async def process_family(message: types.Message, state: FSMContext):
    await state.update_data(family=message.text)
    await message.answer("Telefon raqamingizni kiriting (raqam formatida):")
    await state.set_state(Registration.waiting_for_phone)


@router.message(Registration.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)

    terms = (
        "Quyidagi qonun-qoidalar bilan tanishing:\n"
        "1. Siz shaxsiy ma'lumotlaringizni to'g'ri kiritishingiz kerak.\n"
        "2. Hujjatlarni dona dona qilib, ifodali o'qish lozim.\n\n"
        "Quyidagi PDF hujjatlarni tanlang:"
    )

    keyboard = get_pdf_selection_keyboard(PDF_FILES)
    await message.answer(terms, reply_markup=keyboard)
    await state.set_state(Registration.waiting_for_pdf_choice)
