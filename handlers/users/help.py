from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp
from filters import IsAbiturient, IsUser, IsAdmin, IsStudent


@dp.callback_query_handler(text="помощь")
async def command_help(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.edit_text(f"Здравствуйте, {call.from_user.full_name}, если у вас возникли вопросы, то ознакомьтесь с доступными командами:\n"
                                 f"/start - изменить свою роль\n"                                
                                 f"/timing - посмотреть рассписание\n"
                                 f"/profile - посмотреть профиль\n"
                                 f"/dice - чтобы было\n")


@dp.message_handler(IsUser(), text="/help")
async def command_help_privat(msg: types.Message):
    await msg.answer(f"Здравствуйте, {msg.from_user.full_name}, если у вас возникли вопросы, то ознакомьтесь с доступными командами\n"
                     f"/start - изменить свою роль\n"                                
                     f"/profile - посмотреть профиль\n"
                     f"/dice - чтобы было\n")

@dp.message_handler(IsStudent(), text="/help")
async def command_help_privat(msg: types.Message):
    await msg.answer(f"Здравствуйте, {msg.from_user.full_name}, если у вас возникли вопросы, то ознакомьтесь с доступными командами\n"
                     f"/start - изменить свою роль\n"                                
                     f"/timing - посмотреть рассписание\n"
                     f"/profile - посмотреть профиль\n"
                     f"/dice - чтобы было\n")

@dp.message_handler(IsAbiturient(), text="/help")
async def command_help_privat(msg: types.Message):
    await msg.answer(f"Здравствуйте, {msg.from_user.full_name}, если у вас возникли вопросы, то ознакомьтесь с доступными командами\n"
                     f"/start - изменить свою роль\n"
                     f"/profile - посмотреть профиль\n"
                     f"/dice - чтобы было\n")

@dp.message_handler(IsAdmin(), text="/help_admin")
async def command_help_privat(msg: types.Message):
    await msg.answer(f"Здравствуйте, {msg.from_user.full_name}, если у вас возникли вопросы, то ознакомьтесь с доступными командами\n"
                     f"/add_admin - даёт выбранному пользователю права администратора-модератора\n"
                     f"/delete_admin - удаляет выбранного пользователя из списка администраторов\n"
                     f"/delete_self - удалить самого себя из списка администраторов\n"
                     f"/list_admin - показать список действующих администраторов\n"
                     f"/add_spo - добавить новую дисциплину СПО\n")
