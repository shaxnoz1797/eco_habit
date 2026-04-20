import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from config import BOT_TOKEN
from handlers import start_handler, help_handler

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eco_project.settings')
django.setup()


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.message.register(start_handler, Command("start"))
dp.message.register(help_handler, Command("help"))

async def main():
    print("Bot ishga tushdi 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




