from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
#В массивах мы прописываем ряды кнопок, новый массив - новый ряд
kb_unknown = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/menu"),
        ],
    ],
    resize_keyboard=True
)