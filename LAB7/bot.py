import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer("Привіт! Я ехо-бот 🤖. Надішли мені будь-яке повідомлення — я повторю його!")

@dp.message(F.text)
async def echo(msg: Message):
    await msg.answer(msg.text)

async def main():
    print("✅ Бот запущений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
