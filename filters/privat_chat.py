from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsPrivat(BoundFilter):
    async def check(self, msg: types.Message):
        return msg.chat.type == types.ChatType.PRIVATE