import os
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram import Router
from config import PDF_FILES, PDF_FILES_DIR
from states import Registration

router = Router()


@router.callback_query(F.filter(lambda call: call.data and call.data.startswith("pdf_select")))
async def pdf_selection_handler(callback: types.CallbackQuery, state: FSMContext):
    pdf_id = callback.data.split(":")[1]

    if pdf_id not in PDF_FILES:
        await callback.message.answer("Noma'lum PDF tanlandi. Iltimos, qayta urinib ko'ring.")
        return

    await state.update_data(pdf_id=pdf_id)
    file_path = os.path.join(PDF_FILES_DIR, PDF_FILES[pdf_id])
    await callback.message.answer_document(document=open(file_path, "rb"),
                                           caption=f"Tanlangan PDF: {PDF_FILES[pdf_id]}")

    await callback.message.answer("Iltimos, tanlangan PDF asosida audio yozing va botga yuboring:")
    await state.set_state(Registration.waiting_for_audio)
    await callback.answer()
