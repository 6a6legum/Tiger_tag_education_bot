import logging

from aiogram import Dispatcher

from data.config import ADMINS
# from data.config import IP, user, password, db_name
# import psycopg2

async def on_startup_notify(dp: Dispatcher):
    pass
    # for admin in ADMINS:
    #     try:
    #         await dp.bot.send_message(admin, "Бот Запущен")
    #
    #     except Exception as err:
    #         logging.exception(err)
