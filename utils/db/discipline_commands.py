from asyncpg import UniqueViolationError

from utils.db.db_gino import db
from utils.db.schemas.spo import Spo
from utils.db.schemas.vo_ofo import Vo_ofo
from utils.db.schemas.vo_zfo import Vo_zfo
from utils.db.schemas.vo_ozfo import Vo_ozfo


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

async def add_vo_ozfo(name: str):
    try:
        dis = Vo_ozfo(name=name)
        await dis.create()
    except UniqueViolationError:
        print("направление не добавлено")
async def select_all_spo():
    spo = await Spo.query.order_by(Spo.name.desc()).gino.all()
    return spo

async def select_all_vo_ofo():
    vo_ofo = await Vo_ofo.query.order_by(Vo_ofo.name.desc()).gino.all()
    return vo_ofo

async def select_all_vo_zfo():
    vo_zfo = await Vo_zfo.query.order_by(Vo_zfo.name.desc()).gino.all()
    return vo_zfo

async def select_all_vo_ozfo():
    vo_zfo = await Vo_ozfo.query.order_by(Vo_ozfo.name.desc()).gino.all()
    return vo_zfo
async def select_edu_prog_spo(name):
    prog = await Spo.query.where(Spo.name == name).gino.first()
    return prog

async def update_edu_prog_spo9(name, budget_places, form_of_education, period_of_study, price):
    prog = await select_edu_prog_spo(name)
    await prog.update(budget_places=budget_places, form_of_education=form_of_education, period_of_study=period_of_study, price=price).apply()

async def select_edu_prog_vo_ofo(name):
    prog = await Vo_ofo.query.where(Vo_ofo.name == name).gino.first()
    return prog

async def select_edu_prog_vo_zfo(name):
    prog = await Vo_zfo.query.where(Vo_zfo.name == name).gino.first()
    return prog

async def select_edu_prog_vo_ozfo(name):
    prog = await Vo_ozfo.query.where(Vo_ozfo.name == name).gino.first()
    return prog
async def update_edu_prog_vo_ofo(name, budget_places, period_of_study, price, examination, entrance_test, comment):
    prog = await select_edu_prog_vo_ofo(name)
    await prog.update(budget_places=budget_places, period_of_study=period_of_study,  price=price, examination=examination, entrance_test=entrance_test, comment=comment).apply()

async def update_edu_prog_vo_zfo(name, budget_places, period_of_study, price, examination, entrance_test, comment):
    prog = await select_edu_prog_vo_zfo(name)
    await prog.update(budget_places=budget_places, period_of_study=period_of_study,  price=price, examination=examination, entrance_test=entrance_test, comment=comment).apply()

async def update_edu_prog_vo_ozfo(name, budget_places, period_of_study, price, examination, entrance_test, comment):
    prog = await select_edu_prog_vo_ozfo(name)
    await prog.update(budget_places=budget_places, period_of_study=period_of_study,  price=price, examination=examination, entrance_test=entrance_test, comment=comment).apply()
async def delete_vo(name, form):
    try:
        if form == "ОФО":
            spec = Vo_ofo(name=name)
            await spec.delete()
        elif form == "ЗФО":
            spec = Vo_zfo(name=name)
            await spec.delete()
        elif form == "ОЗФО":
            spec = Vo_ozfo(name=name)
            await spec.delete()
    except Exception:
        print(f"Удаление направления подготовки {name} не выполнено")

async def delete_spo(name):
    try:
        spec = Spo(name=name)
        await spec.delete()
    except Exception:
        print(f"Удаление направления подготовки {name} не выполнено")

