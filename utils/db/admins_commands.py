from asyncpg import UniqueViolationError
from utils.db.quick_commands import select_user
from utils.db.db_gino import db
from utils.db.schemas.admins import Admins
from utils.db.schemas.user import User


async def add_admin(user_id: int, first_name: str, last_name: str, username: str, status: str):
    try:
        user = Admins(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status)
        await user.create()
    except UniqueViolationError:
        print("Админ не добавлен")

async def select_admin_id(user_id):
    admin = await Admins.query.where(Admins.user_id == user_id).gino.first()
    return admin

async def select_admin_username(username):
    admin = await Admins.query.where(Admins.username == username).gino.first()
    return admin

async def select_all_admins():
    admins = await Admins.query.order_by(Admins.user_id.desc()).gino.all()
    return admins

async def delete_admin(user_id):
    admin2 = Admins(user_id=user_id)
    await admin2.delete()

async def delete_admin_self(user_id):
    admin = Admins(user_id=user_id)
    await admin.delete()

async def invite_admin(user_id):
    try:
        user = await select_user(int(user_id))
        await add_admin(user.user_id, user.first_name, user.last_name, user.username, status="Модератор")
    except Exception:
        print("Пригласить админа не удалось")

