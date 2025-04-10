from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram import Router
from states import Registration
from keyboards import get_confirmation_keyboard
from config import ADMIN_GROUP_ID

router = Router()


@router.message(Registration.waiting_for_audio, F.audio | F.voice)
async def process_audio(message: types.Message, state: FSMContext):

    audio_file = message.voice if message.voice else message.audio
    if not audio_file:
        await message.answer("Iltimos, audio yoki voice fayl yuboring.")
        return


    await state.update_data(audio_file_id=audio_file.file_id)


    confirmation_text = "Yozilgan audio faylni yubormoqchimisiz? Agar tasdiqlasangiz, audio bot admin guruhiga yuboriladi."
    keyboard = get_confirmation_keyboard()
    await message.answer(confirmation_text, reply_markup=keyboard)
    await state.set_state(Registration.waiting_for_confirmation)


@router.callback_query(F.filter(lambda call: call.data and call.data.startswith("audio_confirm")))
async def audio_confirmation_handler(callback: types.CallbackQuery, state: FSMContext, bot: types.Bot):
    response = callback.data.split(":")[1]
    if response == "yes":

        data = await state.get_data()
        name = data.get("name")
        family = data.get("family")
        phone = data.get("phone")
        pdf_id = data.get("pdf_id")
        audio_file_id = data.get("audio_file_id")

        if not audio_file_id and data.get("audio_file_id") is None:
            await callback.message.answer("Audio ma'lumot topilmadi.")
            await state.clear()
            return

        pdf_info = f"PDF ID: {pdf_id}"
        user_info = f"Foydalanuvchi: {name} {family}\nUsername: {callback.from_user.username}\nTelefon: {phone}"
        caption = f"{user_info}\n{pdf_info}"


        await bot.send_message(chat_id=ADMIN_GROUP_ID, text=caption)

        try:
            if callback.message.reply_to_message and callback.message.reply_to_message.audio:
                await bot.send_audio(chat_id=ADMIN_GROUP_ID, audio=audio_file_id)
            else:
                await bot.send_voice(chat_id=ADMIN_GROUP_ID, voice=audio_file_id)
        except Exception as e:
            await bot.send_message(chat_id=ADMIN_GROUP_ID, text=f"Audio yuborishda xatolik: {e}")

        await callback.message.answer("Sizning audio faylingiz adminlar tomonidan ko'rib chiqiladi. Rahmat!")
        await state.clear()
    else:
        await callback.message.answer("Iltimos, audio yozib qayta yuboring:")
        await state.set_state(Registration.waiting_for_audio)
    await callback.answer()
