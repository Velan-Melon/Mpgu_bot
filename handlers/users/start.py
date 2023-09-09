from aiogram import types
from loader import dp
from filters import IsNotActive, IsUser, IsAdmin, IsStudent, IsAbiturient
from keyboards.inline import ikb_begin, ikb_confirm
from utils.misc import rate_limit
from aiogram.types import CallbackQuery
from utils.db import quick_commands as commands




@dp.callback_query_handler (text="начало")
async def command_start(call: CallbackQuery):
    await call.message.edit_text(f"Здравствуйте, {call.from_user.full_name}! \n"
                     f"Ответьте пожалуйста на вопрос, Вы студент, абитуриент или обычный пользователь?", reply_markup=ikb_begin)


@rate_limit(limit=6)
@dp.message_handler(IsNotActive(), text="/start")
async def command_start(msg: types.Message):
    try:
        user = await commands.select_user(msg.chat.id)
    except Exception:
        await commands.add_user(user_id=msg.chat.id,
                                first_name=msg.from_user.first_name,
                                last_name=msg.from_user.last_name,
                                username=msg.from_user.username,
                                status="active")
    await msg.answer(f"Здравствуйте, {msg.from_user.full_name}! \n"
                     f"Ответьте пожалуйста на вопрос, Вы студент, абитуриент или обычный пользователь?", reply_markup=ikb_begin)

@rate_limit(limit=6)
@dp.message_handler(text="/start")
async def command_start(msg: types.Message):
    user = await commands.select_user(msg.from_user.id)
    await msg.answer(f"Здравствуйте, {msg.from_user.full_name}! \n"
                     f"Ваша нынешняя роль {user.role}\n"
                     f"Желаете её изменить?\n"
                     f"ПРИМЕЧАНИЕ: при подтверждении вся информация о Вас будет удалена", reply_markup=ikb_confirm)

