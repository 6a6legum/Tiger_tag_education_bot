from aiogram import executor
# from states.main_program import MainProgramGeneral
from loader import dp
import middlewares, filters, handlers
# import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from data_base import sqlite_db


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    sqlite_db.sql_start()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

