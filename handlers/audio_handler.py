from aiogram import types, F, Bot, Router
from aiogram.fsm.context import FSMContext
from states import Registration
from keyboards import get_confirmation_keyboard
from config import ADMIN_GROUP_ID
from aiogram.utils.markdown import hlink
from config import PDF_FILES

router = Router()


@router.message(Registration.waiting_for_audio, F.audio | F.voice)
async def process_audio(message: types.Message, state: FSMContext):
    if message.voice:
        await state.update_data(audio_file_id=message.voice.file_id, audio_type="voice")
    elif message.audio:
        await state.update_data(audio_file_id=message.audio.file_id, audio_type="audio")
    else:
        await message.answer("Iltimos, audio yoki voice fayl yuboring.")
        return

    confirmation_text = (
        "Yozilgan audio faylni yubormoqchimisiz? Agar tasdiqlasangiz, audio bot admin guruhiga yuboriladi."
    )
    keyboard = get_confirmation_keyboard()
    await message.answer(confirmation_text, reply_markup=keyboard)
    await state.set_state(Registration.waiting_for_confirmation)


@router.callback_query(F.data.startswith("audio_confirm"))
async def audio_confirmation_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    response = callback.data.split(":")[1]
    if response == "yes":

        data = await state.get_data()
        name = data.get("name")
        family = data.get("family")
        phone = data.get("phone")
        pdf_id = data.get("pdf_id")
        audio_file_id = data.get("audio_file_id")

        if not audio_file_id:
            await callback.message.answer("Audio ma'lumot topilmadi.")
            await state.clear()
            return

        pdf_entry = PDF_FILES.get(pdf_id, {})
        pdf_name = pdf_entry.get("file_name", "Nomaʼlum PDF")

        user = callback.from_user
        if user.username:
            user_display = f"@{user.username}"
        else:
            user_display = hlink("Profilga havola", f"tg://user?id={user.id}")

        caption = (
            f"<b>Foydalanuvchi:</b> {name} {family}\n"
            f"<b>Username:</b> {user_display}\n"
            f"<b>Telefon:</b> {phone}\n"
            f"<b>Tanlangan PDF:</b> {pdf_name} (ID: {pdf_id})"
        )

        try:
            if callback.message.reply_to_message and callback.message.reply_to_message.audio:
                await bot.send_audio(chat_id=ADMIN_GROUP_ID, audio=audio_file_id, caption=caption, parse_mode="HTML")
            else:
                await bot.send_voice(chat_id=ADMIN_GROUP_ID, voice=audio_file_id, caption=caption, parse_mode="HTML")
        except Exception as e:
            await bot.send_message(chat_id=ADMIN_GROUP_ID, text=f"Audio yuborishda xatolik: {e}")

        await callback.message.answer("Sizning audio faylingiz adminlar tomonidan ko'rib chiqiladi. Rahmat!")
        await state.clear()
    else:
        await callback.message.answer("Iltimos, audio yozib qayta yuboring:")
        await state.set_state(Registration.waiting_for_audio)

    await callback.answer()
