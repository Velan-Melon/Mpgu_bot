import asyncio
from aiogram import types
from loader import dp
from utils.misc import rate_limit
from filters import IsStudent, IsAdmin



@rate_limit(limit=3)
@dp.message_handler(IsAdmin(), text="/dice")
async def command_dice(msg: types.Message):
    emoj = await msg.reply_dice()
    msg = await msg.answer(text="Ждём")
    await asyncio.sleep(4)
    if emoj.dice.value == 6:
        await msg.edit_text("Удача на твоей стороне, сынок!")
    else:
        await msg.edit_text("Попробуй еще раз, чемпион")
