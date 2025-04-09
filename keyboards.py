from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_pdf_selection_keyboard(pdf_files: dict) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    for pdf_id, file_name in pdf_files.items():
        keyboard.insert(InlineKeyboardButton(text=f"PDF {pdf_id}", callback_data=f"pdf_select:{pdf_id}"))
    return keyboard


def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Ha, yuboring", callback_data="audio_confirm:yes"),
        InlineKeyboardButton(text="Yo'q, qayta yozaman", callback_data="audio_confirm:no")
    )
    return keyboard
