from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from states.main_program import MainProgramGeneral
from loader import dp, bot
from data_base import sqlite_db
import random

def random_correct_texts():
    texts = ["Погнали дальше!", "Реши и отстальные проблемы на дороге!", "Продвигаемся дальше"]
    i = random.randint(0, 2)
    return texts[i]

def random_correct_gifs():
    texts = ["ok1.mp4", "ok2.mp4", "ok3.mp4", "ok4.mp4"]
    i = random.randint(0, 3)
    return texts[i]

def random_wrong_texts():
    texts = ["Дальше будет лучше!\nНаверное", "Проблемы ещё не закончились", "Время идти дальше"]
    i = random.randint(0, 2)
    return texts[i]

def random_wrong_gifs():
    texts = ["bad1.mp4", "bad2.mp4", "bad3.mp4", "bad4.mp4"]
    i = random.randint(0, 3)
    return texts[i]

def random_thinking_gifs():
    texts = ["q1.mp4", "q2.mp4", "q3.mp4", "q4.mp4", "q5.mp4"]
    i = random.randint(0, 4)
    return texts[i]

@dp.message_handler(text="Погнали 🚗", state=MainProgramGeneral.quiz_welcome_user)
async def start_lesson(message: types.Message,  state: FSMContext):
    await message.answer("Как и в любой области, в дорожном хозяйстве существуют свои термины и определения. Нужно в них разобраться.")

    video_name = random_thinking_gifs()
    video = open(video_name, 'rb')
    await bot.send_video((types.User.get_current()).id, video)

    start_buttons = ["Логин", "Пароль", "Карта СКУД", "USB-Token"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Что из перечисленного не является аутентификатором?", reply_markup=keyboard)
    await MainProgramGeneral.quiz_q1_user.set()


@dp.message_handler(state=MainProgramGeneral.quiz_q1_user)
async def start_lesson(message: types.Message,  state: FSMContext):
    answer = message.text
    valid = ["Логин", "Пароль", "Карта СКУД", "USB-Token"]
    if answer in valid:
        if answer=="Пароль":
            await message.answer("Молодец! Пароль действительно не является аутентификатором.")
            await message.answer(random_correct_texts())
            video_name = random_correct_gifs()
            video = open(video_name, 'rb')
            await bot.send_video((types.User.get_current()).id, video)
        else:
            await message.answer("Ты ответил неправильно( Аутентификатором не может являться только пароль.")
            await message.answer(random_wrong_texts())
            video_name = random_wrong_gifs()
            video = open(video_name, 'rb')
            await bot.send_video((types.User.get_current()).id, video)

        await message.answer("Что-то пошло не так и образовался большой затор. Все машины встали. Но на одной из дорог движение в норме.")
        start_buttons = ["Twitter", "Facebook", "Instagram", "WhatsApp"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)
        await message.answer("При большом сбое в начале октября какая из компаний пострадала менее всего?", reply_markup=keyboard)
        await MainProgramGeneral.quiz_q2_user.set()


@dp.message_handler(state=MainProgramGeneral.quiz_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    answer = message.text
    valid = ["Twitter", "Facebook", "Instagram", "WhatsApp"]
    if answer in valid:
        if answer == "Twitter":
            await message.answer("Так точно! Из списка только Twitter по-прежнему работал.")
            await message.answer(random_correct_texts())
            video_name = random_correct_gifs()
            video = open(video_name, 'rb')
            await bot.send_video((types.User.get_current()).id, video)
        else:
            await message.answer("Нет, это был Twitter. В тот день все там шутили о Facebook.")
            await message.answer(random_wrong_texts())
            video_name = random_wrong_gifs()
            video = open(video_name, 'rb')
            await bot.send_video((types.User.get_current()).id, video)

        await message.answer(
            "3)	На нашей дороге образовалась большая яма, нужно найти причины.")
        start_buttons = ["Крот", "Червь", "Зомби", "Жук"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)
        await message.answer("Как называется заражённый компьютер, ресурсы которого контролируются злоумышленником без ведома владельца?",
                             reply_markup=keyboard)
        await MainProgramGeneral.quiz_q3_user.set()

@dp.message_handler(state=MainProgramGeneral.quiz_q3_user)
async def start_lesson(message: types.Message, state: FSMContext):
    answer = message.text
    valid = ["Крот", "Червь", "Зомби", "Жук"]
    if answer in valid:
        if answer == "Зомби":
            await message.answer("Конечно же это зомби, ты прав.🧟️")
            await message.answer(random_correct_texts())
            # video_name = random_correct_gifs()
            # video = open(video_name, 'rb')
            # await bot.send_video((types.User.get_current()).id, video)
        else:
            await message.answer("Нет, это зомби. Правда он не кусается.")
            # await message.answer(random_wrong_texts())
            # video_name = random_wrong_gifs()
            # video = open(video_name, 'rb')
            # await bot.send_video((types.User.get_current()).id, video)


        start_buttons = ["Вернуться на главную⬅"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)
        await message.answer("Ты прошёл все вопросы, которые есть на данный момент. Возвращайся позднее",
                             reply_markup=keyboard)