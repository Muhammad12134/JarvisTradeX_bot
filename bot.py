import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
LANG = os.getenv("LANG", "ru")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    for tf in ['5m', '10m', '15m', '30m']:
        builder.button(text=tf, callback_data=f"timeframe:{tf}")
    builder.adjust(2)
    await message.answer("📊 Выберите таймфрейм для сигнала:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("timeframe"))
async def signal_handler(callback_query: types.CallbackQuery):
    tf = callback_query.data.split(":")[1]
    signal = "🟢 BUY" if tf in ['5m', '10m'] else "🔴 SELL"
    await bot.send_message(chat_id=CHANNEL_ID, text=f"📈 [{tf}] Сигнал: {signal}")
    await callback_query.answer(f"Сигнал {signal} отправлен в канал!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
