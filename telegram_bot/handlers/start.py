from aiogram import types
from aiogram.filters import Command
from keyboards.reply import currency_keyboard

async def start_handler(msg: types.Message):
    kb = currency_keyboard()
    await msg.answer("Вибери валюту:", reply_markup=kb)
