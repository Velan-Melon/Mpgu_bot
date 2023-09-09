import asyncio

from aiogram import types
from loader import dp

from data import config
from utils.db import quick_commands as commands
from utils.db.db_gino import db


async def db_insert(user_id, first_name, last_name, username, role):
    try:
        await commands.select_user(user_id)
    except Exception:
        await commands.add_user(user_id=user_id,
                                first_name=first_name,
                                last_name=last_name,
                                username=username,
                                status="active",
                                role=role)




