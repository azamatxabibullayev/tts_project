from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_pdf_selection_keyboard(pdf_files: dict) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=file["file_name"], callback_data=f"pdf_select:{pdf_id}")]
        for pdf_id, file in pdf_files.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(text="Ha, yuboring", callback_data="audio_confirm:yes"),
        InlineKeyboardButton(text="Yo'q, qayta yozaman", callback_data="audio_confirm:no")
    ]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
