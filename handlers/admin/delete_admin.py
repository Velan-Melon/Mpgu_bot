from filters import IsAdmin
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import state_admin
from utils.db import admins_commands
from utils.db import quick_commands


@dp.message_handler(IsAdmin(), text='/delete_admin')
async def delete_admin_func(msg: types.Message):
    await msg.answer("Введите username человека, которого хотите удалить из администраторов\n"
                     "\n"
                     "username это ссылка на пользователя, выглядит вот так: @username\n"
                     "\n"
                     "(Этот человек должен активировать бота самостоятельно, чтобы иметь возможность получить статус администратора)")
    await state_admin.admin.adm_step_2.set()

@dp.message_handler(state=state_admin.admin.adm_step_2)
async def delete_admin_func(msg: types.Message, state: FSMContext):
    answer = msg.text[1:]
    try:
        name = await quick_commands.select_username(answer)
        print(f"id пользователя, которого удаляют из администраторов: {name.user_id}")
        await admins_commands.delete_admin(name.user_id)
        await dp.bot.send_message(chat_id=name.user_id, text="Поздравляю, Вы больше не являетесь администратором")
        print(f"пользователь {answer} больше не является администратором")
        await msg.answer(f"пользователь {answer} больше не является администратором")
        await state_admin.admin.adm_step_2.set()
        await state.finish()
    except Exception:
        await msg.answer("По каким-то причинам удалить администратора не получилось, проверьте username")
        print(Exception)

@dp.message_handler(IsAdmin(), text= "/delete_self")
async def delete_admin_self(msg: types.Message):
    try:
        await admins_commands.delete_admin_self(msg.from_user.id)
        await msg.answer("Вы больше не администратор")
        print(f"Пользователь {msg.from_user.id}, {msg.from_user.username}, {msg.from_user.first_name} юольше не является администратором")
    except Exception:
        print(Exception)
        await msg.answer("Произошла ошибка")