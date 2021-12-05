import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from states.main_program import MainProgramGeneral
from loader import dp, bot
from data_base import sqlite_db
import random
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink



def random_thinking_gifs():
    texts = ["q1.mp4", "q2.mp4", "q3.mp4", "q4.mp4", "q5.mp4"]
    i = random.randint(0, 4)
    return texts[i]
def random_case(num_cases):
    i = random.randint(0, num_cases-1)
    return i

@dp.message_handler(text="Помчались 🚎", state=MainProgramGeneral.cases_welcome_user)
async def start_lesson(message: types.Message,  state: FSMContext):
    start_buttons = ["Последний кейс", "Рандомный кейс", "Вернуться на главную⬅"]

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Последний кейс"),

            ],
            [
                KeyboardButton(text="Рандомный кейс"),
            ],
            [
                KeyboardButton(text="Вернуться на главную⬅"),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer("Ты хочешь посмотреть последний кейс или рандомный?", reply_markup=keyboard)
    await MainProgramGeneral.cases_q1_user.set()
    # video_name = random_thinking_gifs()
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)





@dp.message_handler(text="Последний кейс", state=MainProgramGeneral.cases_q1_user)
async def start_case(message: types.Message,  state: FSMContext):

        # video_name = random_thinking_gifs()
        # video = open(video_name, 'rb')
        # await bot.send_video((types.User.get_current()).id, video)
        with open("news_dict.json") as file:
            news_dict = json.load(file)
        for k, v in sorted(news_dict.items())[-1:]:
            news = f"{hbold(v['article_date_time'])}\n" \
                   f"{hlink(v['article_title'], v['article_url'])}"
            await message.answer(news)

@dp.message_handler(text="Рандомный кейс", state=MainProgramGeneral.cases_q1_user)
async def start_case(message: types.Message,  state: FSMContext):

        # video_name = random_thinking_gifs()
        # video = open(video_name, 'rb')
        # await bot.send_video((types.User.get_current()).id, video)
        with open("news_dict.json") as file:
            news_dict = json.load(file)
            chosen_case = random_case(len(sorted(news_dict.items())))

        for k, v in sorted(news_dict.items())[chosen_case:chosen_case+1]:
            news = f"{hbold(v['article_date_time'])}\n" \
                   f"{hlink(v['article_title'], v['article_url'])}"
            await message.answer(news)

