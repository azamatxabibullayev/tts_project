import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from config import BOT_TOKEN
from handlers import registration, pdf_handler, audio_handler


async def main():
    storage = MemoryStorage()
    bot_properties = DefaultBotProperties(parse_mode="HTML")
    bot = Bot(token=BOT_TOKEN, default=bot_properties)
    dp = Dispatcher(storage=storage)

    dp.include_router(registration.router)
    dp.include_router(pdf_handler.router)
    dp.include_router(audio_handler.router)

    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
