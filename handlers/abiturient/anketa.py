from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery
from states import anketa
from utils.db import quick_commands as command

@dp.callback_query_handler(text="анкета")
async def anketa_(call: CallbackQuery):
    await call.message.edit_text(f"Отлично! сейчас Вам будет представлен ряд небольших вопросов, на которые Вы должны ответить, чтобы мы понимали какое направление Вам подойдёт, а по завершению Вы сможете ознакомиться с интересющей Вас информацией")
    await anketa.start.set()


@dp.message_handler(state=anketa.start)
async def start(msg: types.Message):
    kb_start_anketa = ReplyKeyboardMarkup(row_width=2,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="9 классов"),
                                             KeyboardButton(text="11 классов"),
                                         ],
                                         [
                                             KeyboardButton(text="Среднее профессиональное образование"),
                                             KeyboardButton(text="Высшее образование"),
                                         ]
                                     ])
    await msg.answer("Какое у вас образование?", reply_markup=kb_start_anketa)
    if msg.text == "9 классов":
        await anketa.spo_9_class
    if msg.text == "11 классов":
        await anketa.start_b
    if msg.text == "Среднее профессиональное образование":
        await anketa.vo_na_spo_start
    if msg.text == "Высшее образование":
        await anketa.start_d

@dp.message_handler(state=anketa.start_b)
async def start_a(msg: types.Message):
    kb_start_anketa_b = ReplyKeyboardMarkup(row_width=2,
                                          keyboard=[
                                              [
                                                  KeyboardButton(text="Среднее профессиональное образование"),
                                                  KeyboardButton(text="Высшее образование"),
                                              ]
                                          ])
    await msg.answer("Выбирите образование, которое Вас интересует", reply_markup=kb_start_anketa_b)
    if msg.text == "Среднее профессиональное образование":
        await anketa.spo_11_class_start
    if msg.text == "Высшее образование":
        await anketa.vo_11_class_start

@dp.message_handler(state=anketa.start_d)
async def start_a(msg: types.Message):
    kb_start_anketa_d = ReplyKeyboardMarkup(row_width=2,
                                          keyboard=[
                                              [
                                                  KeyboardButton(text="Высшее образование"),
                                                  KeyboardButton(text="Магистратура"),
                                              ]
                                          ])
    await msg.answer("Выбирите образование, которое Вас интересует", reply_markup=kb_start_anketa_d)
    if msg.text == "Магистратура":
        await anketa.magistrat
    if msg.text == "Высшее образование":
        await anketa.vo_na_vo_start

@dp.message_handler(state=anketa.spo_9_class)
async def start(msg: types.Message):
    kb_spo_9_class_anketa = ReplyKeyboardMarkup(row_width=2,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="Педагогическое"),
                                             KeyboardButton(text="Экономическое"),
                                         ],
                                         [
                                             KeyboardButton(text="Программирование"),
                                             KeyboardButton(text="Юридическое"),
                                             KeyboardButton(text="Дизайн"),
                                         ]
                                     ])
    await msg.answer("Какое направление Вас интересует?", reply_markup=kb_spo_9_class_anketa)
    if msg.text == "Педагогическое":
        await anketa.spo_9_class_a
    if msg.text == "Экономическое":
        await anketa.spo_9_class_b
    if msg.text == "Программирование":
        await anketa.spo_9_class_c
    if msg.text == "Юридическое":
        await anketa.spo_9_class_d
    if msg.text == "Дизайн":
        await anketa.spo_9_class_e

@dp.message_handler(state=anketa.spo_9_class_a)
async def start(msg: types.Message):
    kb_spo_9_class_anketa = ReplyKeyboardMarkup(row_width=2,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="Преподавание в начальных классах"),
                                             KeyboardButton(text="Коррекционная педагогика в начальном образовании"),
                                         ],
                                         [
                                             KeyboardButton(text="Дошкольное образование"),
                                             KeyboardButton(text="Назад"),
                                         ]
                                     ])
    await msg.answer("Выберите то что Вас интересует", reply_markup=kb_spo_9_class_anketa)
    if msg.text == "Преподавание в начальных классах":
        await anketa.spo_9_class_a1
    if msg.text == "Коррекционная педагогика в начальном образовании":
        await anketa.spo_9_class_a2
    if msg.text == "Дошкольное образование":
        await anketa.spo_9_class_a3
    if msg.text == "Назад":
        await anketa.spo_9_class_start
