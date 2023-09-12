from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_confirm = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Готово"),
                KeyboardButton(text="Отмена"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )