from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

from utils.db import quick_commands as commands


from loader import dp
@dp.callback_query_handler(text="студент")
async def student(call: CallbackQuery):
    await commands.update_role(call.message.chat.id, "Студент")
    await commands.add_student(call.message.chat.id)

    ikb_choise = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="Подтвердить", callback_data="регистрация"),
                                              InlineKeyboardButton(text="Отмена", callback_data="начало")
                                          ],
                                      ])
    await call.message.edit_text(f"Отлично! если Вы готовы пройти регистрацию, то нажмите кнопку подтверждения, если Вы нажали сюда случайно, "
                     f"то нажмите кнопку отмены", reply_markup=ikb_choise)


@dp.callback_query_handler(text="абитуриент")
async def abiturient(call: CallbackQuery):
    await commands.update_role(call.message.chat.id, "Абитуриент")
    await commands.add_abiturient(call.message.chat.id)
    ikb_choise = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="Подтвердить", callback_data="анкета"),
                                              InlineKeyboardButton(text="Отмена", callback_data="начало")
                                          ],
                                      ])
    await call.message.edit_text(f"Добро пожаловать в Ставропольский филиал МПГУ, Готовы заполнить анкету?", reply_markup=ikb_choise)

@dp.callback_query_handler(text="пользователь")
async def user(call: CallbackQuery):
    await commands.update_role(call.message.chat.id, "Пользователь")
    ikb_choise = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="Подтвердить", callback_data="пользователь"),
                                              InlineKeyboardButton(text="Отмена", callback_data="начало")
                                          ],
                                      ])
    await call.message.edit_text(f"Вам как обычному пользователю предоставлена навигация по сайту\n"
                                 f"Если Вы ошиблись, нажмите кнопку \"Отмена\", в другом случае подтвердите своё действие", reply_markup=ikb_choise)

