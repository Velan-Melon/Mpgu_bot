from filters import IsAdmin
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import vo_vo_ofo, vo11_ofo, vo_spo_ofo
from keyboards.default import kb_cancel, kb_confirm


from utils.db import discipline_commands as command
data = []
@dp.message_handler(IsAdmin(), text='/add_vo_ofo')
async def update_vo(msg: types.Message):
    await msg.answer("Введите название образовательной программы, которую Вы хотите добавить, либо нажмите отмена", reply_markup=kb_cancel)
    await vo11_ofo.vo11_ofo_step_7.set()
@dp.message_handler(state=vo11_ofo.vo11_ofo_step_7)
async def add_vo(msg: types.Message, state: FSMContext):
    if msg.text != "Отмена":
        await command.add_vo_ofo(msg.text)
    await state.finish()


@dp.message_handler(IsAdmin(), text='/update_vo_ofo')
async def update_spo(msg: types.Message):
    kb_spo = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="11"),
                KeyboardButton(text="СПО"),
                KeyboardButton(text="ВО"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await msg.answer("Вы хотите исправить список ВО после 9 или 11?", reply_markup=kb_spo)
    await vo11_ofo.vo11_ofo_step_start.set()

@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_7)
async def update_spo(msg: types.Message):
    kb_spo = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="11"),
                KeyboardButton(text="СПО"),
                KeyboardButton(text="ВО"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await msg.answer("Вы хотите исправить список ВО после 9 или 11?", reply_markup=kb_spo)
    await vo11_ofo.vo11_ofo_step_start.set()
@dp.message_handler(state=vo11_ofo.vo11_ofo_step_start)
async def add_vo(msg: types.Message, state: FSMContext):
    string = ""
    kb_vo = ReplyKeyboardMarkup(
        keyboard=[
            [
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    all_ofo = await command.select_all_vo_ofo()
    for name_spec in all_ofo:
        string += name_spec.name + '\n'
        kb_vo.insert(types.KeyboardButton(text=str(name_spec.name)))

    await msg.answer(f"Напишите название дисциплины из предложенных:\n"
                     f"------------------------------\n"
                     f"{string}"
                     f"------------------------------", reply_markup=kb_vo)
    if msg.text == "11":
        await vo11_ofo.vo11_ofo_step_1.set()
    if msg.text == "СПО":
        await vo_spo_ofo.vo_spo_ofo_step_1.set()
    if msg.text == "ВО":
        await vo_vo_ofo.vo_vo_ofo_step_1.set()

@dp.message_handler(state=vo11_ofo.vo11_ofo_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer1 = msg.text
    data.append(answer1)
    await msg.answer("Напишите есть ли бюджетные места")
    await vo11_ofo.vo11_ofo_step_3.set()


@dp.message_handler(state=vo11_ofo.vo11_ofo_step_3)
async def state1(msg: types.Message, state: FSMContext):
    answer3 = msg.text
    data.append(answer3)

    await msg.answer("Укажите срок обучения")

    await vo11_ofo.vo11_ofo_step_4.set()

@dp.message_handler(state=vo11_ofo.vo11_ofo_step_4)
async def state2(msg: types.Message, state: FSMContext):
    answer4 = msg.text
    data.append(answer4)

    await msg.answer(f"Укажите цену за год в рублях")
    await vo11_ofo.vo11_ofo_step_5.set()

@dp.message_handler(state=vo11_ofo.vo11_ofo_step_5)
async def state2(msg: types.Message, state: FSMContext):
    answer5 = msg.text
    data.append(answer5)

    await msg.answer(f"Какие экзамены или вступительные экзамены необходимы для поступления?")
    await vo11_ofo.vo11_ofo_step_6.set()


@dp.message_handler(state=vo11_ofo.vo11_ofo_step_6)
async def state2(msg: types.Message, state: FSMContext):
    answer6 = msg.text
    data.append(answer6)
    await msg.answer(f"Пожалуйста проверьте, всё ли заполнено правильно:\n"
                     f"------------------------------\n"
                     f"Название: <b><u>{data[0]}</u></b>\n"
                     f"Бюджетные места: <b><u>{data[1]}</u></b>\n"
                     f"Срок обучения: <b><u>{data[2]}</u></b>\n"
                     f"Стоимость обучения в год: <b><u>{data[3]}</u></b>\n"
                     f"Экзамены: <b><u>{data[4]}</u></b>\n"
                     f"------------------------------\n"
                     f"Если всё готово, нажмите на кнопку \"Готово\", если Вы допустили ошибку, нажмите \"Отмена\"", reply_markup=kb_confirm)
    await vo11_ofo.vo11_ofo_step_finish.set()

@dp.message_handler(state=vo11_ofo.vo11_ofo_step_finish)
async def state2(msg: types.Message, state: FSMContext):
    if msg.text == "Готово":
        await command.update_edu_prog_vo11_ofo(data[0], data[1], data[2], data[3], data[4])
        data.clear()
        await msg.answer(f"Изменения сохранены", reply_markup=types.ReplyKeyboardRemove())
        await vo11_ofo.vo11_ofo_step_finish.set()
    else:
        await msg.answer("Изменения не сохранены", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()





@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer1 = msg.text
    data.append(answer1)
    await msg.answer("Напишите есть ли бюджетные места")
    await vo_spo_ofo.vo_spo_ofo_step_3.set()

@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_3)
async def state1(msg: types.Message, state: FSMContext):
    answer3 = msg.text
    data.append(answer3)

    await msg.answer("Укажите срок обучения")

    await vo_spo_ofo.vo_spo_ofo_step_4.set()

@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_4)
async def state2(msg: types.Message, state: FSMContext):
    answer4 = msg.text
    data.append(answer4)

    await msg.answer(f"Укажите цену за год в рублях")
    await vo_spo_ofo.vo_spo_ofo_step_5.set()

@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_5)
async def state2(msg: types.Message, state: FSMContext):
    answer5 = msg.text
    data.append(answer5)

    await msg.answer(f"Какие экзамены или вступительные экзамены необходимы для поступления?")
    await vo_spo_ofo.vo_spo_ofo_step_6.set()


@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_6)
async def state2(msg: types.Message, state: FSMContext):
    answer6 = msg.text
    data.append(answer6)
    await msg.answer(f"Пожалуйста проверьте, всё ли заполнено правильно:\n"
                     f"------------------------------\n"
                     f"Название: <b><u>{data[0]}</u></b>\n"
                     f"Бюджетные места: <b><u>{data[1]}</u></b>\n"
                     f"Срок обучения: <b><u>{data[2]}</u></b>\n"
                     f"Стоимость обучения в год: <b><u>{data[3]}</u></b>\n"
                     f"Экзамены: <b><u>{data[4]}</u></b>\n"
                     f"------------------------------\n"
                     f"Если всё готово, нажмите на кнопку \"Готово\", если Вы допустили ошибку, нажмите \"Отмена\"",
                     reply_markup=kb_confirm)
    await vo_spo_ofo.vo_spo_ofo_step_finish.set()


@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_finish)
async def state2(msg: types.Message, state: FSMContext):
    if msg.text == "Готово":
        await command.update_edu_prog_vo_on_spo_ofo(data[0], data[1], data[2], data[3], data[4])
        data.clear()
        await msg.answer(f"Изменения сохранены", reply_markup=types.ReplyKeyboardRemove())
        await vo_spo_ofo.vo_spo_ofo_step_finish.set()
    else:
        await msg.answer("Изменения не сохранены", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(state=vo_vo_ofo.vo_vo_ofo_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer1 = msg.text
    data.append(answer1)
    await msg.answer("Напишите есть ли бюджетные места")
    await vo_vo_ofo.vo_vo_ofo_step_3.set()

@dp.message_handler(state=vo_vo_ofo.vo_vo_ofo_step_3)
async def state1(msg: types.Message, state: FSMContext):
    answer3 = msg.text
    data.append(answer3)

    await msg.answer("Укажите срок обучения")

    await vo_vo_ofo.vo_vo_ofo_step_4.set()

@dp.message_handler(state=vo_vo_ofo.vo_vo_ofo_step_4)
async def state2(msg: types.Message, state: FSMContext):
    answer4 = msg.text
    data.append(answer4)

    await msg.answer(f"Укажите цену за год в рублях")
    await vo_vo_ofo.vo_vo_ofo_step_5.set()

@dp.message_handler(state=vo_vo_ofo.vo_vo_ofo_step_5)
async def state2(msg: types.Message, state: FSMContext):
    answer5 = msg.text
    data.append(answer5)

    await msg.answer(f"Какие экзамены или вступительные экзамены необходимы для поступления?")
    await vo_vo_ofo.vo_vo_ofo_step_6.set()


@dp.message_handler(state=vo_vo_ofo.vo_vo_ofo_step_6)
async def state2(msg: types.Message, state: FSMContext):
    answer6 = msg.text
    data.append(answer6)
    await msg.answer(f"Пожалуйста проверьте, всё ли заполнено правильно:\n"
                     f"------------------------------\n"
                     f"Название: <b><u>{data[0]}</u></b>\n"
                     f"Бюджетные места: <b><u>{data[1]}</u></b>\n"
                     f"Срок обучения: <b><u>{data[2]}</u></b>\n"
                     f"Стоимость обучения в год: <b><u>{data[3]}</u></b>\n"
                     f"Экзамены: <b><u>{data[4]}</u></b>\n"
                     f"------------------------------\n"
                     f"Если всё готово, нажмите на кнопку \"Готово\", если Вы допустили ошибку, нажмите \"Отмена\"",
                     reply_markup=kb_confirm)
    await vo_vo_ofo.vo_vo_ofo_step_finish.set()


@dp.message_handler(state=vo_vo_ofo.vo_vo_ofo_step_finish)
async def state2(msg: types.Message, state: FSMContext):
    if msg.text == "Готово":
        await command.update_edu_prog_vo_on_vo_ofo(data[0], data[1], data[2], data[3], data[4])
        data.clear()
        await msg.answer(f"Изменения сохранены", reply_markup=types.ReplyKeyboardRemove())
        await vo_vo_ofo.vo_vo_ofo_step_finish.set()
    else:
        await msg.answer("Изменения не сохранены", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
