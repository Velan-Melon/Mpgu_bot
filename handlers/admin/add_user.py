from filters import IsAdmin
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import state_admin
from utils.db import admins_commands


@dp.message_handler(IsAdmin(), text='/add_admin')
async def add_admin(msg: types.Message):
    await msg.answer("Введите id человека, которому хотите выдать статус администратора\n"
                     "(Этот человек должен активировать бота самостоятельно, чтобы иметь возможность получить статус администратора)")
    await state_admin.admin.adm_step_1.set()

@dp.message_handler(state=state_admin.admin.adm_step_1)
async def add_admin(msg: types.Message, state: FSMContext):
    answer = msg.text
    try:
        await admins_commands.invite_admin(answer)
        await dp.bot.send_message(chat_id=answer, text="Поздравляю, Вас назначили администратором")
        await msg.answer("Админ добавлен")
        await state_admin.admin.adm_step_1.set()
        await state.finish()
    except:
        await msg.answer("По каким-то причинам добавить админа не получилось, проверьте id")