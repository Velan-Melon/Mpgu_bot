from aiogram import types
from loader import dp
from filters import IsPrivat

@dp.message_handler(IsPrivat())
async def command_error(msg: types.Message):
    await msg.answer(f"К сожалению такой команды нет, введите /help, чтобы увидеть список доступных команд")
