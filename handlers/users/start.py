from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from states.user_info import IntroTest, IntroTestUser, IntroTestOperator, IntroTestAdmin
from loader import dp, bot
from data_base import sqlite_db
# from keyboards.default import change_data
from utils.check_authorization import auth

@dp.message_handler(CommandStart(), state='*')
@auth
async def bot_start(message: types.Message):
    await message.answer("Приветствуем тебя на нашем курсе по кибербезопасности! 👋🏻\nПеред начал просим тебя ответить на пару вопросов, чтобы подобрать программу.")
    await message.answer("Как тебя зовут?")
    await IntroTest.name.set()
    # await message.answer(f"Привет, {message.from_user.full_name}!")




@dp.message_handler(state=IntroTest.name)
async def answer_q1(message: types.Message, state: FSMContext):
    user = types.User.get_current()
    chat_id = user.id
    await state.update_data(id=chat_id)
    answer = message.text
    await state.update_data(name=answer)
    # async with state.proxy() as data:
    #     data["name"] = answer
    start_buttons = ["1", "2", "3"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("К какой из этих категорий ты бы себя отнёс?\n 1. Пользователь\n 2. Оператор\n 3. Администратор", reply_markup=keyboard)

    await IntroTest.categoryWorker.set()


@dp.message_handler(state=IntroTest.categoryWorker)
async def answer_q2(message: types.Message, state: FSMContext):
    if message.text=="1" or message.text=="2" or message.text=="3":
        await state.update_data(category=message.text)
        start_buttons = ["Да", "Нет"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)
        await message.answer("Хотел ли ты получать рассылку?", reply_markup=keyboard)
        await IntroTest.recieveNews.set()
    else:
        await message.reply("Пожалуйста, введи корректный ответ.")
        start_buttons = ["1", "2", "3"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer(
            "К какой из этих категорий ты бы себя отнёс?\n 1. Пользователь\n 2. Оператор\n 3. Администратор",
            reply_markup=keyboard)

        await IntroTest.categoryWorker.set()

    # data = await state.get_data()
    # name = data.get("name")



@dp.message_handler(state=IntroTest.recieveNews)
async def answer_q3(message: types.Message, state: FSMContext):
    if message.text=="Да" or message.text=="Нет":
        await state.update_data(recieve=message.text)
        await state.update_data(intro_test=0)
        # data = await state.get_data()
        # name = data.get("name")

        start_buttons = ["Начать тестирование❗️"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)
        try:
            await sqlite_db.sql_add_command(state)
            await state.finish()
            await message.answer(
                "Отлично. Нажми на кнопку, когда будешь готов пройти входное тестирование!",
                reply_markup=keyboard)

            video = open("agutin.gif", 'rb')
            await bot.send_video((types.User.get_current()).id, video)

            user = types.User.get_current()
            chat_id = user.id
            db_row = await sqlite_db.sql_read(chat_id)
            category = db_row[0][2]
            if category == "1":
                await IntroTestUser.q0.set()
            if category == "2":
                await IntroTestOperator.q0.set()
            if category == "3":
                await IntroTestAdmin.q0.set()
            # await message.answer(
            #     "Отлично, вы прошли тест. Нажмите на кнопку, когда будете готовы начать входное тестирование!",
            #     reply_markup=keyboard)
        except:
            change_data = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Да"),
                        KeyboardButton(text="Нет"),
                    ],
                ],
                resize_keyboard=True
            )
            await message.answer("Ты уже вводил свои данные. Уверен, что хочешь их поменять?", reply_markup=change_data)
            await IntroTest.changeData.set()
    else:
        await message.reply("Пожалуйста, введи корректный ответ.")
        start_buttons = ["Да", "Нет"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)
        await message.answer("Хотел ли ты получать рассылку?", reply_markup=keyboard)
        await IntroTest.recieveNews.set()

        #Сделать клавиатуру да/нет
    # await message.answer(name+" "+category +" "+ recieve+" ")
    # await state.finish()
    # await message.answer("Отлично, вы прошли тест. Нажмите на кнопку, когда будете готовы начать входное тестирование!",
    #                      reply_markup=keyboard)

@dp.message_handler(text="Да", state=IntroTest.changeData)
async def change_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get("id")
    await sqlite_db.sql_update_users(state, id)
    start_buttons = ["Начать тестирование❗️"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Ты успешно поменял информацию о себе.\nНажми на кнопку, когда будешь готов снова пройти входное тестирование!", reply_markup=keyboard)
    video =  open("agutin.gif", 'rb')
    await bot.send_video((types.User.get_current()).id, video)

    user = types.User.get_current()
    chat_id = user.id
    db_row = await sqlite_db.sql_read(chat_id)
    category = db_row[0][2]
    if category == "1":
        await IntroTestUser.q0.set()
    if category == "2":
        await IntroTestOperator.q0.set()
    if category == "3":
        await IntroTestAdmin.q0.set()


@dp.message_handler(text="Нет", state=IntroTest.changeData)
async def change_data(message: types.Message):
    await message.answer("Отлично, информация о тебе осталась прежней, продолжай заниматься на курсе!", reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(text="Начать тестирование❗️")
# async def start_test(message: types.Message):
#     user = types.User.get_current()
#     chat_id = user.id
#     db_row = await sqlite_db.sql_read(chat_id)
#     category = db_row[0][2]
#     if category=="1":
#
#     # await message.answer("Отлично, информация о тебе осталась прежней, продолжай заниматься на курсе!", reply_markup=ReplyKeyboardRemove())