from aiogram import types
#Здесь можно прописать различные команды
async def set_defolt_commands(dp):
        await dp.bot.set_my_commands([
            types.BotCommand('start', 'Запустить бота'),
            types.BotCommand('help', 'Помощь'),
            types.BotCommand('dice', "Игра с кубиком"),
            types.BotCommand('profile', 'Получить свои данные')
        ])