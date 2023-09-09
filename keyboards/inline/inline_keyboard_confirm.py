from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_confirm = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Да", callback_data="начало"),
                                        InlineKeyboardButton(text="Нет", callback_data="помощь")
                                    ]
                                ])