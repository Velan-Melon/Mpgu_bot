from filters import IsAdmin
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import spo9, spo11

from utils.db import discipline_commands as command
data = []
@dp.message_handler(IsAdmin(), text='/add_spo')
async def update_spo(msg: types.Message):
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
    await spo9.spo9_step_6.set()
@dp.message_handler(state=spo9.spo9_step_6)
async def add_spo(msg: types.Message, state: FSMContext):
    if msg.text == "Отмена":
        await state.finish()
    else:
        await command.add_spo(msg.text)
    await state.finish()


@dp.message_handler(IsAdmin(), text='/update_spo')
async def update_spo(msg: types.Message):
    await msg.answer("Напишите название дисциплины")
    spo11.spo11_step_1.set()

@dp.message_handler(state=spo9.spo9_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer1 = msg.text
    data.append(answer1)
    await msg.answer("Напишите есть ли бюджетные места")
    await spo9.spo9_step_2.set()

@dp.message_handler(state=spo9.spo9_step_2)
async def state1(msg: types.Message, state: FSMContext):
    answer2 = msg.text
    data.append(answer2)
    await msg.answer("Какие присутсвуют формы обучения?")
    await spo9.spo9_step_3.set()

@dp.message_handler(state=spo9.spo9_step_3)
async def state1(msg: types.Message, state: FSMContext):
    answer3 = msg.text
    data.append(answer3)

    await msg.answer("Укажите срок обучения")

    await spo9.spo9_step_4.set()

@dp.message_handler(state=spo9.spo9_step_4)
async def state2(msg: types.Message, state: FSMContext):
    answer4 = msg.text
    data.append(answer4)

    await msg.answer(f"Укажите цену за год в рублях")
    await spo9.spo9_step_5.set()


@dp.message_handler(state=spo9.spo9_step_5)
async def state2(msg: types.Message, state: FSMContext):
    answer5 = msg.text
    data.append(answer5)
    await command.update_edu_prog_spo9(data[0],data[1], data[2], data[3], data[4])
    data.clear()
    await msg.answer(f"готово")
    await spo9.spo9_step_5.set()
    await state.finish()





