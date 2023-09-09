from aiogram import types
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@dp.message_handler(text="/timing")
async def command_timing(msg: types.Message):
    ikb_timing = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="Рассписание", url="https://drive.google.com/drive/folders/1r1IaDUGp60NbcBVnrlqLcix5lT9YaN1a"),
                                          ],
                                      ])
    await msg.answer(text="нажмите на кнопку чтобы перейти по ссылке", reply_markup=ikb_timing)
    await asyncio.sleep(1)
    await msg.answer(text="Если у Вас появились затруднения, то можете обратиться за помощью, прописав команду /timing_help")