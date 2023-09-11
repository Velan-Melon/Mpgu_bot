from asyncpg import UniqueViolationError

from utils.db.db_gino import db
from utils.db.schemas.spo import Spo
from utils.db.schemas.vo_ofo import Vo_ofo
from utils.db.schemas.vo_zfo import Vo_zfo


async def add_spo(name: str):
    try:
        dis = Spo(name=name)
        await dis.create()
    except UniqueViolationError:
        print("направление не добавлено")

async def add_vo_ofo(name: str):
    try:
        dis = Vo_ofo(name=name)
        await dis.create()
    except UniqueViolationError:
        print("направление не добавлено")

async def add_vo_zfo(name: str):
    try:
        dis = Vo_zfo(name=name)
        await dis.create()
    except UniqueViolationError:
        print("направление не добавлено")


async def select_edu_prog_spo(name):
    prog = await Spo.query.where(Spo.name == name).gino.first()
    return prog

async def update_edu_prog_spo9(name, budget_places_9, form_of_education_9, period_of_study_9, price_9):
    prog = await select_edu_prog_spo(name)
    await prog.update(budget_places_9=budget_places_9, form_of_education_9=form_of_education_9, period_of_study_9=period_of_study_9,  price_9=price_9).apply()

async def update_edu_prog_spo11(name, budget_places_11, form_of_education_11, period_of_study_11, price_11):
    prog = await select_edu_prog_spo(name)
    await prog.update(budget_places_11=budget_places_11, form_of_education_11=form_of_education_11, period_of_study_11=period_of_study_11,  price_11=price_11).apply()

async def select_edu_prog_vo_ofo(name):
    prog = await Vo_ofo.query.where(Vo_ofo.name == name).gino.first()
    return prog

async def select_edu_prog_vo_zfo(name):
    prog = await Vo_zfo.query.where(Vo_zfo.name == name).gino.first()
    return prog

async def update_edu_prog_vo11_ofo(name, budget_places_vo11, form_of_education_vo11, period_of_study_vo11, price_vo11, examination_on_11):
    prog = await select_edu_prog_vo_ofo(name)
    await prog.update(budget_places_vo11=budget_places_vo11, form_of_education_vo11=form_of_education_vo11, period_of_study_vo11=period_of_study_vo11,  price_vo11=price_vo11, examination_on_11=examination_on_11).apply()

async def update_edu_prog_vo_on_spo_ofo(name, budget_places_vo_on_spo, form_of_education_vo_on_spo, period_of_study_vo_on_spo, price_vo_on_spo, examination_on_spo):
    prog = await select_edu_prog_vo_ofo(name)
    await prog.update(budget_places_vo_on_spo=budget_places_vo_on_spo, form_of_education_vo_on_spo=form_of_education_vo_on_spo, period_of_study_vo_on_spo=period_of_study_vo_on_spo,  price_vo_on_spo=price_vo_on_spo, examinationon_spo=examination_on_spo).apply()

async def update_edu_prog_vo_on_vo_ofo(name, budget_places_vo_on_vo, form_of_education_vo_on_vo, period_of_study_vo_on_vo, price_vo_on_vo, examination_on_vo):
    prog = await select_edu_prog_vo_ofo(name)
    await prog.update(budget_places_vo_on_vo=budget_places_vo_on_vo, form_of_education_vo_on_vo=form_of_education_vo_on_vo, period_of_study_vo_on_vo=period_of_study_vo_on_vo,  price_vo_on_vo=price_vo_on_vo, examination_on_vo=examination_on_vo).apply()

async def update_edu_prog_vo11_zfo(name, budget_places_vo11, form_of_education_vo11, period_of_study_vo11, price_vo11, examination_on_11):
    prog = await select_edu_prog_vo_zfo(name)
    await prog.update(budget_places_vo11=budget_places_vo11, form_of_education_vo11=form_of_education_vo11, period_of_study_vo11=period_of_study_vo11,  price_vo11=price_vo11, examination_on_11=examination_on_11).apply()

async def update_edu_prog_vo_on_spo_zfo(name, budget_places_vo_on_spo, form_of_education_vo_on_spo, period_of_study_vo_on_spo, price_vo_on_spo, examination_on_spo):
    prog = await select_edu_prog_vo_zfo(name)
    await prog.update(budget_places_vo_on_spo=budget_places_vo_on_spo, form_of_education_vo_on_spo=form_of_education_vo_on_spo, period_of_study_vo_on_spo=period_of_study_vo_on_spo,  price_vo_on_spo=price_vo_on_spo, examinationon_spo=examination_on_spo).apply()

async def update_edu_prog_vo_on_vo_zfo(name, budget_places_vo_on_vo, form_of_education_vo_on_vo, period_of_study_vo_on_vo, price_vo_on_vo, examination_on_vo):
    prog = await select_edu_prog_vo_zfo(name)
    await prog.update(budget_places_vo_on_vo=budget_places_vo_on_vo, form_of_education_vo_on_vo=form_of_education_vo_on_vo, period_of_study_vo_on_vo=period_of_study_vo_on_vo,  price_vo_on_vo=price_vo_on_vo, examination_on_vo=examination_on_vo).apply()

