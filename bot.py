import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
LANG = os.getenv("LANG", "ru")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

timeframe_keyboard = InlineKeyboardMarkup(row_width=2)
for tf in ['5m', '10m', '15m', '30m']:
    timeframe_keyboard.insert(InlineKeyboardButton(f"{tf}", callback_data=f"timeframe:{tf}"))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("📊 Выберите таймфрейм для сигнала:", reply_markup=timeframe_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith("timeframe"))
async def signal_handler(callback_query: types.CallbackQuery):
    tf = callback_query.data.split(":")[1]
    # Здесь будет логика анализа (заглушка)
    signal = "🟢 BUY" if tf in ['5m', '10m'] else "🔴 SELL"
    await bot.send_message(chat_id=CHANNEL_ID, text=f"📈 [{tf}] Сигнал: {signal}")
    await callback_query.answer(f"Сигнал {signal} отправлен в канал!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)