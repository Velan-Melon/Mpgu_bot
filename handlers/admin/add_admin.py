from filters import IsAdmin
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import state_admin
from utils.db import admins_commands
from utils.db import quick_commands


@dp.message_handler(IsAdmin(), text='/add_admin')
async def add_admin(msg: types.Message):
    await msg.answer("Введите username человека, которому хотите выдать статус администратора\n"
                     "\n"
                     "username это ссылка на пользователя, выглядит вот так: @username\n"
                     "\n"
                     "(Этот человек должен активировать бота самостоятельно, чтобы иметь возможность получить статус администратора)")
    await state_admin.admin.adm_step_1.set()

@dp.message_handler(state=state_admin.admin.adm_step_1)
async def add_admin(msg: types.Message, state: FSMContext):
    answer = msg.text[1:]
    try:
        name = await quick_commands.select_username(answer)
        print(f"id пользователя, которого добавляют в телеграмм: {name.user_id}")
        await admins_commands.invite_admin(name.user_id)
        await dp.bot.send_message(chat_id=name.user_id, text="Поздравляю, Вас назначили администратором, воспользуйтесь командой /help_admin чтобы узнать свои возможности")
        print(f"пользователь {answer} теперь является администратором")
        await msg.answer(f"пользователь {answer} теперь является администратором")
        await state_admin.admin.adm_step_1.set()
        await state.finish()
    except:
        await msg.answer("По каким-то причинам добавить админа не получилось, проверьте id")