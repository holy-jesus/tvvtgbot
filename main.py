import asyncio
import os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from TakVamVidno import TVV
from TakVamVidno.extractors import OpenAIOCR, prepare_images
from TakVamVidno.providers import OpenAIProvider


load_dotenv()

dp = Dispatcher()
# tvv = TVV(OpenAIProvider(), OpenAIOCR())


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Привет! Отправь мне картинку с документом, а я тебе отправлю анализ этого документа.")


@dp.message()
async def catch_all(message: Message):
    print(message.photo)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=os.getenv("telegram_token"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)

asyncio.run(main())