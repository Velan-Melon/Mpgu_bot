from filters import IsAdmin
from aiogram.types import ReplyKeyboardMarkup
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import vo11_zfo
from keyboards.default import kb_cancel, kb_confirm


from utils.db import discipline_commands as command
data = []
@dp.message_handler(IsAdmin(), text='/add_vo_zfo')
async def update_vo(msg: types.Message):
    await msg.answer("Введите название образовательной программы, которую Вы хотите добавить, либо нажмите отмена", reply_markup=kb_cancel)
    await vo11_zfo.vo11_zfo_step_start.set()
@dp.message_handler(state=vo11_zfo.vo11_zfo_step_start)
async def add_vo(msg: types.Message, state: FSMContext):
    if msg.text != "Отмена":
        await command.add_vo_zfo(msg.text)
    await state.finish()


@dp.message_handler(IsAdmin(), text='/update_vo_zfo')
async def update_spo(msg: types.Message):
    string = ""
    kb_vo = ReplyKeyboardMarkup(
        keyboard=[
            [
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    all_zfo = await command.select_all_vo_zfo()
    for name_spec in all_zfo:
        string += name_spec.name + '\n'
        kb_vo.insert(types.KeyboardButton(text=str(name_spec.name)))

    await msg.answer(f"Напишите название дисциплины из предложенных:\n"
                     f"------------------------------\n"
                     f"{string}"
                     f"------------------------------", reply_markup=kb_vo)

    await vo11_zfo.vo11_zfo_step_1.set()

@dp.message_handler(state=vo11_zfo.vo11_zfo_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer1 = msg.text
    data.append(answer1)
    await msg.answer("Напишите есть ли бюджетные места")
    await vo11_zfo.vo11_zfo_step_2.set()


@dp.message_handler(state=vo11_zfo.vo11_zfo_step_2)
async def state1(msg: types.Message, state: FSMContext):
    answer2 = msg.text
    data.append(answer2)

    await msg.answer("Укажите срок обучения")

    await vo11_zfo.vo11_zfo_step_3.set()

@dp.message_handler(state=vo11_zfo.vo11_zfo_step_3)
async def state2(msg: types.Message, state: FSMContext):
    answer3 = msg.text
    data.append(answer3)

    await msg.answer(f"Укажите цену за год в рублях")
    await vo11_zfo.vo11_zfo_step_4.set()

@dp.message_handler(state=vo11_zfo.vo11_zfo_step_4)
async def state2(msg: types.Message, state: FSMContext):
    answer4 = msg.text
    data.append(answer4)

    await msg.answer(f"Какие экзамены необходимы для поступления после 11 класса?")
    await vo11_zfo.vo11_zfo_step_5.set()

@dp.message_handler(state=vo11_zfo.vo11_zfo_step_5)
async def state2(msg: types.Message, state: FSMContext):
    answer5 = msg.text
    data.append(answer5)

    await msg.answer(f"Какие вступительные экзамены необходимы для поступления?")
    await vo11_zfo.vo11_zfo_step_6.set()

@dp.message_handler(state=vo11_zfo.vo11_zfo_step_6)
async def state2(msg: types.Message, state: FSMContext):
    answer6 = msg.text
    data.append(answer6)
    await msg.answer(f"Хотите оставить какой-нибудь комментарий, если нет, то просто напишите \"<b>нет</b>\"")
    await vo11_zfo.vo11_zfo_step_7.set()


@dp.message_handler(state=vo11_zfo.vo11_zfo_step_7)
async def state2(msg: types.Message, state: FSMContext):
    answer7 = msg.text
    data.append(answer7.lower())
    await msg.answer(f"Пожалуйста проверьте, всё ли заполнено правильно:\n"
                     f"------------------------------\n"
                     f"Название: <b><u>{data[0]}</u></b>\n"
                     f"Бюджетные места: <b><u>{data[1]}</u></b>\n"
                     f"Срок обучения: <b><u>{data[2]}</u></b>\n"
                     f"Стоимость обучения в год: <b><u>{data[3]}</u></b>\n"
                     f"Экзамены после 11: <b><u>{data[4]}</u></b>\n"
                     f"Вступительные экзамены: <b><u>{data[5]}</u></b>\n"
                     f"Комментарий: <b><u>{data[6]}</u></b>\n"
                     f"------------------------------\n"
                     f"Если всё готово, нажмите на кнопку \"Готово\", если Вы допустили ошибку, нажмите \"Отмена\"",
                     reply_markup=kb_confirm)
    await vo11_zfo.vo11_zfo_step_finish.set()

@dp.message_handler(state=vo11_zfo.vo11_zfo_step_finish)
async def state2(msg: types.Message, state: FSMContext):
    if msg.text == "Готово":
        await command.update_edu_prog_vo_zfo(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        await msg.answer(f"Изменения сохранены", reply_markup=types.ReplyKeyboardRemove())
        await vo11_zfo.vo11_zfo_step_finish.set()
    else:
        await msg.answer("Изменения не сохранены", reply_markup=types.ReplyKeyboardRemove())
    data.clear()
    await state.finish()

