from asyncpg import UniqueViolationError

from utils.db.db_gino import db
from utils.db.schemas.spo import Spo


async def add_spo(name: str):
    try:
        dis = Spo(name=name)
        await dis.create()
    except UniqueViolationError:
        print("пользователь не добавлен")
async def select_edu_prog_spo(name):
    prog = await Spo.query.where(Spo.name == name).gino.first()
    return prog

async def update_edu_prog_spo9(name, budget_places_9, form_of_education_9, period_of_study_9, price_9):
    prog = await select_edu_prog_spo(name)
    await prog.update(budget_places_9=budget_places_9, form_of_education_9=form_of_education_9, period_of_study_9=period_of_study_9,  price_9=price_9).apply()

async def update_edu_prog_spo11(name, budget_places_11, form_of_education_11, period_of_study_11, price_11):
    prog = await select_edu_prog_spo(name)
    await prog.update(budget_places_11=budget_places_11, form_of_education_11=form_of_education_11, period_of_study_11=period_of_study_11,  price_11=price_11).apply()

