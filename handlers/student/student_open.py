from loader import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler (text="студент_открыт")
async def command_student_open(call: CallbackQuery):

    await call.message.edit_text(f"Здравствуйте, {call.from_user.full_name}! \n"
                     f"Вы успешно прошли регистрацию!\n"
                     f"Выберете необходимую Вам команду:\n"
                                 f"/timing - открывает рассписание")
