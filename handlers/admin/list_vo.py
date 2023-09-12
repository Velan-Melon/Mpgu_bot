from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from filters import IsAdmin
from loader import dp
from aiogram import types
from utils.db import discipline_commands as command
from states.state_list import list_vo



@dp.message_handler(IsAdmin(), text='/list_vo')
async def add_spec(msg: types.Message):
    string_ofo = ""
    string_zfo = ""
    string_ozfo = ""
    kb_vo_ofo = ReplyKeyboardMarkup(
        keyboard=[
            [
            ]
        ],
        resize_keyboard=True,
    )
    all_ofo = await command.select_all_vo_ofo()
    for name_spec_ofo in all_ofo:
        string_ofo += name_spec_ofo.name + '\n'
        kb_vo_ofo.insert(types.KeyboardButton(text=str(name_spec_ofo.name + " ОФО")))
    all_zfo = await command.select_all_vo_zfo()
    for name_spec_zfo in all_zfo:
        string_zfo += name_spec_zfo.name + '\n'
        kb_vo_ofo.insert(types.KeyboardButton(text=str(name_spec_zfo.name + " ЗФО")))
    all_ozfo = await command.select_all_vo_ozfo()
    for name_spec_ozfo in all_ozfo:
        string_ozfo += name_spec_ozfo.name + '\n'
        kb_vo_ofo.insert(types.KeyboardButton(text=str(name_spec_ozfo.name + " ОЗФО")))
    else:
        kb_vo_ofo.add(types.KeyboardButton(text="Отмена"))
        kb_vo_ofo.insert(types.KeyboardButton(text="Удаление"))



    await msg.answer(f"Вот список всех специальностей:\n"
                     f"------------------------------\n"
                     f"Очная форма обучения:\n"
                     f"\n<b>{string_ofo}</b>\n"
                     f"------------------------------\n"
                     f"Заочная форма обучения:\n"
                     f"\n<b>{string_zfo}</b>"
                     f"------------------------------\n"
                     f"Очно-заочная форма обучения:\n"
                     f"\n<b>{string_ozfo}</b>\n"
                     f"------------------------------\n"
                     f"Выберите для получения информации\n", reply_markup=kb_vo_ofo)
    await list_vo.vo_step_1.set()
@dp.message_handler(state=list_vo.vo_step_1)
async def add_spec(msg: types.Message, state: FSMContext):
    answer = msg.text
    info_string = ""
    if answer == "Отмена":
        await msg.answer("Выход из просмотра", reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    elif answer == "Удаление":
        
        await msg.answer("Вы перешли в режим редактирования, отправьте название специальности, которую необходимо удалить")
        await list_vo.vo_step_2.set()
    else:
        if answer.find("ОФО") != -1:
            info = await command.select_edu_prog_vo_ofo(answer[:-4])
            info_string = f"""
Название: <b>{info.name}</b>
Бюджетные места: <b>{info.budget_places}</b>
Форма обучения: <b>{info.form_of_education}</b>
Период обучения: <b>{info.period_of_study}</b>
Цена обучения за год: <b>{info.price}</b>
Необходимые экзамены: <b>{info.examination}</b>
Вступительные испытания: <b>{info.entrance_test}</b>
Комментарий: <b>{info.comment}</b>"""

        if answer.find("ЗФО") != -1 and answer.find("ОЗФО") == -1:
            info = await command.select_edu_prog_vo_zfo(answer[:-4])
            info_string = f"""
Название: <b>{info.name}</b>
Бюджетные места: <b>{info.budget_places}</b>
Форма обучения: <b>{info.form_of_education}</b>
Период обучения: <b>{info.period_of_study}</b>
Цена обучения за год: <b>{info.price}</b>
Необходимые экзамены: <b>{info.examination}</b>
Вступительные испытания: <b>{info.entrance_test}</b>
Комментарий: <b>{info.comment}</b>"""
        if answer.find("ОЗФО") != -1:
            print(answer[:-5])
            info = await command.select_edu_prog_vo_ozfo(answer[:-5])
            info_string = f"""
Название: <b>{info.name}</b>
Бюджетные места: <b>{info.budget_places}</b>
Форма обучения: <b>{info.form_of_education}</b>
Период обучения: <b>{info.period_of_study}</b>
Цена обучения за год: <b>{info.price}</b>
Необходимые экзамены: <b>{info.examination}</b>
Вступительные испытания: <b>{info.entrance_test}</b>
Комментарий: <b>{info.comment}</b>"""
        await msg.answer(info_string)
@dp.message_handler(state=list_vo.vo_step_2)
async def add_spec(msg: types.Message, state: FSMContext):
    count = 0
    answer = msg.text
    if answer == "Отмена":
        await msg.answer("Выход из из режима редактирования")
        await list_vo.vo_step_1.set()
    if answer == "Удаление":
        await msg.answer("Вы уже в режиме редактирования, выберите направление для удаления")
    else:
        if answer.find("ОФО") != -1:
            await command.delete_vo(answer[:-4], "ОФО")
        if answer.find("ЗФО") != -1 and answer.find("ОЗФО") == -1:
            await command.delete_vo(answer[:-4], "ЗФО")
        if answer.find("ОЗФО") != -1:
            await command.delete_vo(answer[:-5], "ОЗФО")
        if answer != "Отмена":
            await msg.answer(f"Специальность {answer} удалена")


