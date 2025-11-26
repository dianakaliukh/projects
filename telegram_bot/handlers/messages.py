from aiogram import types
from keyboards.reply import CURRENCIES
from handlers.callbacks import get_rate

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
