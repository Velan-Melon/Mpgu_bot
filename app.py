#app это файл который запускает бота
import loader

async def on_startup(dp):

    import filters
    filters.setup(dp)
    import middlewares
    middlewares.setup(dp)

    from loader import db
    from utils.db.db_gino import on_starup
    print("подключение к базе данных")
    await on_starup(dp)

    await db.gino.create_all()

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_defolt_commands
    await set_defolt_commands(dp)
    print("Бот запущен")



if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)