from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from filters import IsAdmin
from loader import dp
from aiogram import types
from utils.db import discipline_commands as command
from states.state_list import list_spo


@dp.message_handler(IsAdmin(), text='/list_spo')
async def add_spec(msg: types.Message):
    string_spo = ""
    kb_spo = ReplyKeyboardMarkup(
        keyboard=[
            [
            ]
        ],
        resize_keyboard=True
    )
    all_spo = await command.select_all_spo()
    for name_spec_spo in all_spo:
        string_spo += name_spec_spo.name + '\n'
        kb_spo.insert(types.KeyboardButton(text=str(name_spec_spo.name)))

    else:
        kb_spo.add(types.KeyboardButton(text="Отмена"))
        kb_spo.insert(types.KeyboardButton(text="Удаление"))

    await msg.answer(f"Вот список всех специальностей:\n"
                     f"------------------------------\n"
                     f"Очная форма обучения:\n"
                     f"\n<b>{string_spo}</b>\n"
                     f"------------------------------\n"
                     f"Выберите для получения информации\n", reply_markup=kb_spo)
    await list_spo.spo_step_1.set()


@dp.message_handler(state=list_spo.spo_step_1)
async def add_spec(msg: types.Message, state: FSMContext):
    answer = msg.text
    if answer == "Отмена":
        await msg.answer("Выход из просмотра", reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    elif answer == "Удаление":

        await msg.answer(
            "Вы перешли в режим редактирования, отправьте название специальности, которую необходимо удалить")
        await list_spo.spo_step_2.set()
    else:
        try:
            info = await command.select_edu_prog_spo(answer)
            info_string = f"""
Название: <b>{info.name}</b>
Бюджетные места: <b>{info.budget_places_9}</b>
Форма обучения: <b>{info.form_of_education_9}</b>
Период обучения: <b>{info.period_of_study_9}</b>
Цена обучения за год: <b>{info.price_9}</b>"""
            await msg.answer(info_string)
        # Комментарий: <b>{info.comment}</b>
        except Exception:
            await msg.answer("Такой специальности не существует")




@dp.message_handler(state=list_spo.spo_step_2)
async def add_spec(msg: types.Message, state: FSMContext):

    answer = msg.text
    if answer == "Отмена":
        await msg.answer("Выход из из режима редактирования")
        await list_spo.spo_step_1.set()
    if answer == "Удаление":
        await msg.answer("Вы уже в режиме редактирования, выберите направление для удаления")
    else:
            await command.delete_spo(answer)
            if answer != "Отмена":
                await msg.answer(f"Специальность {answer} удалена")


