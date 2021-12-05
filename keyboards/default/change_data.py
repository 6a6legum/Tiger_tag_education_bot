from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

change_data = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text="Да"),
          KeyboardButton(text="Нет"),
        ],
    ],
    resize_keyboard=True
)