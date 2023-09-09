from aiogram import types
from loader import dp

hello = [
    "Привет",
    "привет"
]

@dp.message_handler(text=hello)
async def command_hello(msg: types.Message):
    await msg.answer(f"У тебя какие-то проблемы?")
