from filters import IsAdmin
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import vo_vo_ofo, vo11_ofo, vo_spo_ofo

from utils.db import discipline_commands as command
data = []
@dp.message_handler(IsAdmin(), text='/add_vo_ofo')
async def update_vo(msg: types.Message):
    kb_spo = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отмена"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await msg.answer("Введите название образовательной программы, которую Вы хотите добавить, либо нажмите отмена", reply_markup=kb_spo)
    await vo11_ofo.vo11_ofo_step_6.set()
@dp.message_handler(state=vo11_ofo.vo11_ofo_step_6)
async def add_vo(msg: types.Message, state: FSMContext):
    if msg.text == "Отмена":
        await state.finish()
    else:
        await command.add_vo_ofo(msg.text)
    await state.finish()


@dp.message_handler(IsAdmin(), text='/update_vo')
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
    if msg.text == "11":
        await msg.answer("Напишите название дисциплины")
        await vo11_ofo.vo11_ofo_step_1.set()
    if msg.text == "СПО":
        await msg.answer("Напишите название дисциплины")
        await vo_spo_ofo.vo_spo_ofo_step_1.set()
    if msg.text == "ВО":
        await msg.answer("Напишите название дисциплины")
        await vo_vo_ofo.vo_vo_ofo_step_1.set()
    else:
        await msg.answer("Вы должны выбрать между 11, СПО и ВО")

@dp.message_handler(state=vo11_ofo.vo11_ofo_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer1 = msg.text
    data.append(answer1)
    await msg.answer("Напишите есть ли бюджетные места")
    await vo11_ofo.vo11_ofo_step_2.set()

@dp.message_handler(state=vo11_ofo.vo11_ofo_step_2)
async def state1(msg: types.Message, state: FSMContext):
    answer2 = msg.text
    data.append(answer2)
    await msg.answer("Какие присутсвуют формы обучения?")
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
    await command.update_edu_prog_vo11_ofo(data[0] ,data[1], data[2], data[3], data[4])
    data.clear()
    await msg.answer(f"готово")
    await vo11_ofo.vo11_ofo_step_5.set()
    await state.finish()


@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer1 = msg.text
    data.append(answer1)
    await msg.answer("Напишите есть ли бюджетные места")
    await vo_spo_ofo.vo_spo_ofo_step_2.set()

@dp.message_handler(state=vo_spo_ofo.vo_spo_ofo_step_2)
async def state1(msg: types.Message, state: FSMContext):
    answer2 = msg.text
    data.append(answer2)
    await msg.answer("Какие присутсвуют формы обучения?")
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
    await command.update_edu_prog_vo_on_spo(data[0], data[1], data[2], data[3], answer5)
    print(data)
    data.clear()
    await msg.answer(f"готово")
    await vo_spo_ofo.vo_spo_ofo_step_5.set()
    await state.finish()


