

from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from utils.db import admins_commands as commands

class IsAdmin(BoundFilter):
    async def check(self, msg: types.Message):
        try:
            admin = await commands.select_admin(msg.chat.id)
            if isinstance(admin.user_id, int):
                return True
        except Exception:
            return False


