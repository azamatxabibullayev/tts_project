from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_pdf_selection_keyboard(pdf_files: dict) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=f"PDF {pdf_id}", callback_data=f"pdf_select:{pdf_id}")]
        for pdf_id in pdf_files
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(text="Ha, yuboring", callback_data="audio_confirm:yes"),
        InlineKeyboardButton(text="Yo'q, qayta yozaman", callback_data="audio_confirm:no")
    ]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
