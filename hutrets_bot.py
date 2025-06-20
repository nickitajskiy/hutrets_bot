# Бот для тгк Хытрец
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

API_TOKEN = '7680076686:AAH42InLnm6A0zHMzUdDtroc3sQpvOZc25s'
CHANNEL_ID = '@hutretz'
WEBAPP_URL = 'https://loft-kovka.ru/gallery'

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
router = Router()

@router.message(Command("post"))
async def post_instruction(message: Message):
    await message.answer("Пришли фото с подписью — и я опубликую его в канал с кнопкой «Каталог».")

@router.message(F.photo)
async def handle_photo(message: Message):
    caption = message.caption or "Без подписи"

    # Кнопка с URL (откроется в Telegram, если правильно настроен WebApp)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛠️ Наши изделия ️", url=WEBAPP_URL)]
    ])

    photo_id = message.photo[-1].file_id

    await bot.send_photo(chat_id=CHANNEL_ID, photo=photo_id, caption=caption, reply_markup=keyboard)

    await message.answer("✅ Пост опубликован с кнопкой!")

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
