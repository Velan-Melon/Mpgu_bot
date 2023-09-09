from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
#В массивах мы прописываем ряды кнопок, новый массив - новый ряд
kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Студент"),
            KeyboardButton(text="Абитуриент"),
        ],
        [
            KeyboardButton(text="Пользователь"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)