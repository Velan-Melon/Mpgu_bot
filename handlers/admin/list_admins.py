from filters import IsAdmin
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import state_admin
from utils.db import admins_commands as commands
from utils.db import quick_commands


@dp.message_handler(IsAdmin(), text='/list_admin')
async def add_admin(msg: types.Message):
    admins = await commands.select_all_admins()
    string2 = ""
    for admin in admins:
        try:
            string = "\n------------------------------\n"+ str("id: " + str(admin.user_id) + "\nusername: @" + str(
                admin.username) + "\nname: " + admin.first_name)
            string2 += string

        except Exception as err:
            print(err)
    await msg.answer("Вот список администраторов:" + string2)
