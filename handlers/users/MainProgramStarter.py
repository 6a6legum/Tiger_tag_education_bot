from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from states.main_program import MainProgramGeneral
from loader import dp, bot
from data_base import sqlite_db
from utils.check_authorization import auth

@dp.message_handler(state=MainProgramGeneral.welcome)
async def before_questions(message: types.Message,  state: FSMContext):
    await  message.answer("Сейчас тебе доступно 3 активности. \n⚫ Во-первых, ты можешь начать проходить небольшие обучающие уроки, в которых ты на практике научишься навыкам кибербезопасности."
                          + "\n⚫ Во-вторых, ты можешь пройти квизы и проверить, свои знания. \n⚫ Наконец, ты можешь прочитать про реальные кейсы из области кибербезопасности.")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Хочу уроки📚"),
            ],
            [
                KeyboardButton(text="Хочу квизы📃"),
            ],
            [
                KeyboardButton(text="Хочу кейсы🧳"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer("Что тебе было бы интересно сделать?", reply_markup=keyboard)
    await MainProgramGeneral.waitingForAnswer.set()

@dp.message_handler(text="Хочу уроки📚", state="*")
@auth
async def start_lesson(message: types.Message):
    user = types.User.get_current()
    chat_id = user.id
    db_row = await sqlite_db.sql_read(chat_id)
    category = db_row[0][2]
    start_buttons = ["Поехали 🚑"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer(
        "Чтобы решать проблемы на дороге тебе будет нужна теория. Сейчас ты преисполнишься необходимыми знаниями.",
        reply_markup=keyboard)
    if category == "1":
        await MainProgramGeneral.lesson_welcome_user.set()
    if category == "2":
        await MainProgramGeneral.lesson_welcome_operator.set()
    if category == "3":
        await MainProgramGeneral.lesson_welcome_admin.set()


@dp.message_handler(text="Хочу квизы📃", state="*")
@auth
async def start_quiz(message: types.Message):
    user = types.User.get_current()
    chat_id = user.id
    db_row = await sqlite_db.sql_read(chat_id)
    category = db_row[0][2]
    start_buttons = ["Погнали 🚗"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Представь, что ты регулируешь происшествия на дороге. Ответь на пару вопросов и реши все образовавшиеся проблемы!", reply_markup=keyboard)
    if category == "1":
        await MainProgramGeneral.quiz_welcome_user.set()
    if category == "2":
        await MainProgramGeneral.quiz_welcome_operator.set()
    if category == "3":
        await MainProgramGeneral.quiz_welcome_admin.set()


@dp.message_handler(text="Хочу кейсы🧳", state="*")
@auth
async def start_cases(message: types.Message):
    user = types.User.get_current()
    chat_id = user.id
    db_row = await sqlite_db.sql_read(chat_id)
    category = db_row[0][2]
    start_buttons = ["Помчались 🚎"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer(
        "Чтобы успешно регулировать происшествия на дороге необходимо учиться и на ошибках других. Сейчас ты сможешь прочитать новости про реальные кейсы из кибербезопасности!",
        reply_markup=keyboard)
    if category == "1":
        await MainProgramGeneral.cases_welcome_user.set()
    if category == "2":
        await MainProgramGeneral.cases_welcome_operator.set()
    if category == "3":
        await MainProgramGeneral.cases_welcome_admin.set()


@dp.message_handler(text="Вернуться на главную⬅", state="*")
@auth
async def start_again(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Хочу уроки📚"),
            ],
            [
                KeyboardButton(text="Хочу квизы📃"),
            ],
            [
                KeyboardButton(text="Хочу кейсы🧳"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer("Что тебе было бы интересно сделать?", reply_markup=keyboard)
    await MainProgramGeneral.waitingForAnswer.set()
