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
        await register.reg_step_2.set()
    await register.reg_step_2.set()


@dp.message_handler(state=register.reg_step_2)
async def state1(msg: types.Message, state: FSMContext):
    answer = msg.text
    kb_curs = ReplyKeyboardMarkup(
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
    await msg.answer("Выберете Ваш курс", reply_markup=kb_curs)
    await register.reg_step_3.set()

@dp.message_handler(state=register.reg_step_3)
async def state1(msg: types.Message, state: FSMContext):
    answer = int(msg.text)
    await command.update_student_curs(msg.from_user.id, answer)
    await msg.answer("Укажите Вашу специальность или направление подготовки, если затрудняетесь, то вот список")
    await msg.answer("СПО:\n"
                    "1. Преподавание в начальных классах\n"
                    "2. Коррекционная педагогика в начальном образовании\n"
                    "3. Дошкольное образование\n"
                    "4. Экономика и бухгалтерский учёт (по отраслям)\n"
                    "5. Право и организация социального обеспечения\n"
                    "6. Информационные системы и программирование\n"
                    "7. Информационные системы (по отраслям)\n"
                    "8. Дизайн (по отраслям)\n"
                    "ВО:\n"
                    "1. Психолого-педагогическое образование (Психология и социальная педагогика)\n"
                    "2. Психолого-педагогическое образование (Психология и педагогика дошкольного образования)\n"
                    "3. Педагогическое образование (Начальное образование)\n"
                    "4. Педпгогическое образование (Дошкольное образование и специальная педагогика)\n"
                    "5. Юриспруденция (Общеправовой профиль)\n"
                    "6. Государственное и муниципальное управление\n"
                    "7. Менеджмент (Организация и управление бизнесом)\n"
                    "8. Менеджмент (Экономика и управление предприятием)\n"
                    "9. Менеджмент (Управление государственным и муниципальным сектором)\n"
                    "10. Прикладная информатика (Прикладная информатика в экономике)\n"
                    "11. Дизайн (Дизайн среды)")
    await register.reg_step_4.set()

@dp.message_handler(state=register.reg_step_4)
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
    await msg.answer(f"Спасибо за уделенное время, регистрация завершена\n", reply_markup=ikb_choise)
    await register.reg_step_4.set()
    await state.finish()
