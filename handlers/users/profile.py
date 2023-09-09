from aiogram import types
from keyboards.inline import ikb_begin
from loader import dp
from utils.db import quick_commands as commands



@dp.message_handler(text="/profile")
async def command_profile(msg: types.Message):
        user = await commands.select_user(msg.from_user.id)
        if user.user_id == 765343682:
            await msg.answer(f"Вы Маркова Полина Алексеевна\n"
                             f"Ваш статус: незамужем.. шучу, {user.role}\n"
                             f"Ты потрясающая кстати")
        if user.user_id == 1122556361:
            await msg.answer(f"Вы .... Так стоп ты здесь чо забыл {user.first_name}\n"
                             f"{user.last_name}, ты же школота ещё, чо поступать думаешь?\n"
                             f"Сдай информатику на 80+ и я подумаю")
        else:
            await msg.answer(f"Вы {user.first_name}\n"
                             f"Ваша роль: {user.role}")

