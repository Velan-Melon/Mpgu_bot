from aiogram import Bot, types, Dispatcher
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.db_gino import db

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

__all__ = ["bot", "storage", "dp", "db"]

#в лоадере прописываются основные свойства бота