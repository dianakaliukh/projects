import aiohttp
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from lab8 import TOKEN

# 10 валют
CURRENCIES = ["USD", "EUR", "GBP", "PLN", "CZK", "CHF", "JPY", "CAD", "AUD", "SEK"]

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КЛАВІАТУРА ---
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=cur) for cur in CURRENCIES[:5]],
        [KeyboardButton(text=cur) for cur in CURRENCIES[5:]]
    ],
    resize_keyboard=True
)

# --- Отримання курсу з API НБУ ---
async def get_rate(currency: str):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"HTTP {resp.status}")

                data = await resp.json()

                # формат відповіді НБУ:
                # [{"r030": 840, "txt": "Долар США", "rate": 41.50, "cc": "USD", "exchangedate": "20.02.2025"}]
                if not data or "rate" not in data[0]:
                    raise RuntimeError(f"Invalid response: {data}")

                return data[0]["rate"]

    except Exception as e:
        raise RuntimeError(f"Error: {e}")

# --- Команда /start ---
@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Вибери валюту:", reply_markup=keyboard)

# --- Обробка натискання валюти ---
@dp.message()
async def currency_handler(msg: types.Message):
    cur = msg.text.upper()

    if cur in CURRENCIES:
        try:
            rate = await get_rate(cur)
            await msg.answer(f"1 {cur} = {rate:.2f} UAH (НБУ)")
        except RuntimeError as e:
            await msg.answer(f"Помилка отримання курсу:\n{e}")
    else:
        await msg.answer("Оберіть валюту з клавіатури.")

# --- Запуск ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
