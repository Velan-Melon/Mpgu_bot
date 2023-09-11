import logging

from aiogram import Dispatcher
from data.config import ADMIN_ID
from utils.db import admins_commands as commands

#Это сообщения, которые будут отправлены админам при запуске бота
async def on_startup_notify(dp: Dispatcher):
    admins = await commands.select_all_admins()
    for admin in admins:
        try:
            text = "Бот активирован"
            await dp.bot.send_message(chat_id=admin.user_id, text=text)
        except Exception as err:
            logging.exception(err)




