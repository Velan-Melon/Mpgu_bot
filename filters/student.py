from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from utils.db import quick_commands as commands

class IsStudent(BoundFilter):
    async def check(self, msg: types.Message):
        try:
            user = await commands.select_user(msg.chat.id)
            if user.role=="Студент":
                return True
        except Exception:
            return False