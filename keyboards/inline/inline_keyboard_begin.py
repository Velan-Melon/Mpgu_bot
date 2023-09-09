from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_begin = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Студент", callback_data="студент"),
                                        InlineKeyboardButton(text="Абитуриент", callback_data="абитуриент")
                                    ],
                                    [
                                        InlineKeyboardButton(text="Пользователь", callback_data="пользователь")
                                    ]
                                ])