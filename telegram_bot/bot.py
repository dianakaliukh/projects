import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from config import TOKEN
from handlers import start_handler, currency_handler

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Реєструємо обробники
dp.message.register(start_handler, CommandStart())
dp.message.register(currency_handler)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
