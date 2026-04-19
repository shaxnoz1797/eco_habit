from aiogram import types

async def start_handler(message: types.Message):
    await message.answer("Salom! Bot ishlayapti 🚀")

async def help_handler(message: types.Message):
    await message.answer("Yordam komandasi")