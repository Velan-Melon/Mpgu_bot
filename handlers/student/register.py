from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery
from states import register

from utils.db import quick_commands as command


@dp.callback_query_handler(text="регистрация")
async def register_(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.edit_text("Регистрация началась, ответьте на следующие вопросы")
    kb_edu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Среднее профессиональное образование (СПО)"),
                KeyboardButton(text="Высшее образование (ВО)"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await call.message.answer("Выбирите проффесиональное образование, которое получаете в настоящий момент",
                              reply_markup=kb_edu)
    await register.reg_step_1.set()


@dp.message_handler(state=register.reg_step_1)
async def state1(msg: types.Message, state: FSMContext):
    answer = msg.text
    kb_form = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Очная форма обучения (ОФО)"),
                KeyboardButton(text="Очно-заочная форма обучения (ОЗФО)"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    kb_form2 = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="после 9 класса"),
                KeyboardButton(text="после 11 класса"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await command.update_student_username(msg.from_user.id, msg.from_user.username)
    await command.update_student_education(msg.from_user.id, answer)
    if answer == "Высшее образование (ВО)":
        await msg.answer(f"Выберите к какой форме обучения Вы относитесь", reply_markup=kb_form)
        await register.reg_step_2.set()
    elif answer == "Среднее профессиональное образование (СПО)":
        await msg.answer(f"Укажите после какого класса Вы поступили", reply_markup=kb_form2)
        await register.reg_step_3.set()


@dp.message_handler(state=register.reg_step_2)
async def state1(msg: types.Message, state: FSMContext):
    answer = msg.text
    kb_curs1 = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1"),
                KeyboardButton(text="2"),
            ],
            [
                KeyboardButton(text="3"),
                KeyboardButton(text="4"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    kb_curs2 = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1"),
                KeyboardButton(text="2"),
            ],
            [
                KeyboardButton(text="3"),
                KeyboardButton(text="4"),
                KeyboardButton(text="5"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await command.update_student_form(msg.from_user.id, answer)
    if answer == "Очная форма обучения (ОФО)":
        await msg.answer(f"Выберете Ваш курс", reply_markup=kb_curs1)
        await register.reg_step_5.set()
    elif answer == "Очно-заочная форма обучения (ОЗФО)":
        await msg.answer(f"Выберете Ваш курс", reply_markup=kb_curs2)
        await register.reg_step_5.set()

@dp.message_handler(state=register.reg_step_3)
async def state1(msg: types.Message, state: FSMContext):
    answer = msg.text
    kb_curs1 = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1"),
                KeyboardButton(text="2"),
            ],
            [
                KeyboardButton(text="3"),
                KeyboardButton(text="4"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await command.update_student_form(msg.from_user.id, answer)
    await msg.answer(f"Выберете Ваш курс", reply_markup=kb_curs1)
    await register.reg_step_4.set()



@dp.message_handler(state=register.reg_step_4)
async def state1(msg: types.Message, state: FSMContext):
    answer = int(msg.text)
    kb_list = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Преподавание в начальных классах"),
                KeyboardButton(text="Коррекционная педагогика начальном образовании"),
            ],

            [
                KeyboardButton(text="Дошкольное образование"),
                KeyboardButton(text="Экономика и бухгалтерский учёт (по отраслям)"),
            ],

            [
                KeyboardButton(text="Право и организация социального обеспечения"),
                KeyboardButton(text="Информационные системы и программирование"),
            ],
            [
                KeyboardButton(text="Информационные системы (по отраслям)"),
                KeyboardButton(text="Дизайн (по отраслям)"),
            ]

        ],
        one_time_keyboard=True
    )
    await command.update_student_curs(msg.from_user.id, answer)
    await msg.answer("Укажите Вашу специальность или направление подготовки", reply_markup=kb_list)
    await register.reg_step_6.set()
@dp.message_handler(state=register.reg_step_5)
async def state1(msg: types.Message, state: FSMContext):
    answer = int(msg.text)
    kb_list = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Психология и социальная педагогика"),
                KeyboardButton(text="Психология и педагогика дошкольного образования"),
            ],

            [
                KeyboardButton(text="Начальное образование"),
                KeyboardButton(text="Дошкольное образование и специальная педагогика"),
            ],

            [
                KeyboardButton(text="Юриспруденция (Общеправовой профиль)"),
                KeyboardButton(text="Государственное и муниципальное управление"),
            ],
            [
                KeyboardButton(text="Организация и управление бизнесом"),
                KeyboardButton(text="Экономика и управление предприятием"),
            ],
            [
                KeyboardButton(text="Управление государственным и муниципальным сектором"),
                KeyboardButton(text="Дизайн (Дизайн среды)"),
            ],
            [
                KeyboardButton(text="Прикладная информатика в экономике"),
            ],
        ],
        one_time_keyboard=True
    )
    await command.update_student_curs(msg.from_user.id, answer)
    await msg.answer("Укажите Вашу специальность или направление подготовки, если затрудняетесь, то вот список", reply_markup=kb_list)
    await register.reg_step_6.set()

@dp.message_handler(state=register.reg_step_6)
async def state2(msg: types.Message, state: FSMContext):
    ikb_choise = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="Подтвердить", callback_data="студент_открыт"),
                                              InlineKeyboardButton(text="Я допустил ошибку!", callback_data="регистрация")
                                          ],
                                      ])
    answer = msg.text
    await command.update_student_speciality(msg.from_user.id, answer)
    student = await command.select_student(msg.from_user.id)
    await msg.answer(f"Готово!\n"
                     f"Пожалуйста перепроверьте свои ответы, и если всё верно: нажмите кнопку подтвердить\n"
                     f"-----------------------\n"
                     f"У Вас {student.education} {student.form}\n"
                     f"Вы на {student.curs} курсе\n"
                     f"И Вы обучаетесь по направлению подготовки {student.speciality}\n"
                     f"-----------------------\n"
                     f"Всё верно?", reply_markup=types.ReplyKeyboardRemove())
    await msg.answer(f"Спасибо за уделенное время, регистрация завершена\n", reply_markup=ikb_choise)

    await register.reg_step_6.set()
    await state.finish()
