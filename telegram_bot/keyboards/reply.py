from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

CURRENCIES = ["USD", "EUR", "GBP", "PLN", "CZK", "CHF", "JPY", "CAD", "AUD", "SEK"]

def currency_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=cur) for cur in CURRENCIES[:5]],
            [KeyboardButton(text=cur) for cur in CURRENCIES[5:]]
        ],
        resize_keyboard=True
    )
