import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers import commands, signals

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
dp.include_router(commands.router)
dp.include_router(signals.router)

WEBHOOK_PATH = "/webhook"
WEBHOOK_PORT = 8080
WEBHOOK_URL = f"https://jarvistradex-bot.onrender.com{WEBHOOK_PATH}"

async def main():
    await bot.set_webhook(WEBHOOK_URL)
    await dp.start_webhook(
        webhook_path=WEBHOOK_PATH,
        bot=bot,
        skip_updates=True,
        host="0.0.0.0",
        port=WEBHOOK_PORT
    )

if __name__ == "__main__":
    asyncio.run(main())
