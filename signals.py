from aiogram import Router, types

router = Router()

@router.message(lambda message: message.text and message.text.lower().startswith("signal"))
async def handle_signal(message: types.Message):
    await message.answer("📈 Получен сигнал. Обрабатываю, сэр!")
