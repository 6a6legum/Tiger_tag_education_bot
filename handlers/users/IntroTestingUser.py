from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from states.user_info import IntroTest, IntroTestUser, IntroTestOperator, IntroTestAdmin
from states.main_program import MainProgramGeneral
from loader import dp, bot
from data_base import sqlite_db


@dp.message_handler(text="Начать тестирование❗️", state=IntroTestUser.q0)
async def before_questions(message: types.Message,  state: FSMContext):
    await  message.answer("Начинаем тест для пользователя")
    start_buttons = ["А", "Б", "В"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("1. Чья ответственность за компрометацию пароля пользователя?\nА. Владелец сервиса\nБ. Клиент\nВ. Зависит от характера атаки", reply_markup=keyboard)
    await IntroTestUser.q1.set()


@dp.message_handler(state=IntroTestUser.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    user = types.User.get_current()
    chat_id = user.id
    await state.update_data(id=chat_id)
    answer = message.text
    if answer=="А" or answer=="Б" or answer=="В":
        await state.update_data(q1=answer)

        start_buttons = ["А", "Б"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("2. Может ли злоумышленник начать атаку на офис компании при неправильно опубликованной фотографии офиса, и компания не имеет публичных ресурсов?\nА. Нет\nБ. Да", reply_markup=keyboard)
        await IntroTestUser.q2.set()

@dp.message_handler(state=IntroTestUser.q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "А" or answer == "Б":
        await state.update_data(q2=answer)

        start_buttons = ["А", "Б", "В"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("3. Популярный сервис AdBlock можно ли использовать в качестве дополнительного эшелона безопасности?\nА. Нет\nБ. Да, в предустановке есть механизмы безопасности\nВ. Да, но при должной настройке", reply_markup=keyboard)
        await IntroTestUser.q3.set()

@dp.message_handler(state=IntroTestUser.q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б" or answer == "В":
        await state.update_data(q3=answer)

        start_buttons = ["А", "Б"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("4. Может ли считаться явно юридически значимым документ, к которому нет подписи отдельным файлом?\nА. Да\nБ. Нет", reply_markup=keyboard)
        await IntroTestUser.q4.set()

@dp.message_handler(state=IntroTestUser.q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б":
        await state.update_data(q4=answer)

        start_buttons = ["А", "Б"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("5. Будет ли подтверждаться подлинность файла при изменении его названия?\nА. Нет\nБ. Да", reply_markup=keyboard)
        await IntroTestUser.q5.set()

@dp.message_handler(state=IntroTestUser.q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б":
        await state.update_data(q5=answer)

        start_buttons = ["А", "Б"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("6. Гарантирует ли наличие соответствия 152-ФЗ у сервиса отсутствия удачных атак на него?\nА. Да\nБ. Нет", reply_markup=keyboard)
        await IntroTestUser.q6.set()

@dp.message_handler(state=IntroTestUser.q6)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б":
        await state.update_data(q6=answer)

        start_buttons = ["А", "Б", "В"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("7. Какому из этих механизмов лучше всего доверять при передачи конфиденциальной информации через мессенджер?\nА. Внутреннее шифрование мессенджера\n Б. Шифрование непосредственно файла\n В. VPN-туннель", reply_markup=keyboard)
        await IntroTestUser.q7.set()

@dp.message_handler(state=IntroTestUser.q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б" or answer == "В":
        await state.update_data(q7=answer)

        start_buttons = ["А", "Б", "В"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("8. Внутренние системы шифрования в Excel можно считать надежным?\nА. Да\nБ. Зависит от выбранного алгоритма шифрования\nВ. Нет", reply_markup=keyboard)
        await IntroTestUser.q8.set()

@dp.message_handler(state=IntroTestUser.q8)
async def answer_q8(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б" or answer == "В":
        await state.update_data(q8=answer)

        start_buttons = ["А", "Б", "В", "Г"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("9. Может ли дубликат грифа конфиденциальности быть скрыт при открытии документа?\nА. Нет\nБ. Да, но юридической силы он не имеет\nВ. Да\nГ. Нет, при отсутствии видимого грифа, скрытого быть не может", reply_markup=keyboard)
        await IntroTestUser.q9.set()

@dp.message_handler(state=IntroTestUser.q9)
async def answer_q9(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б" or answer == "В" or answer == "Г":
        await state.update_data(q9=answer)

        start_buttons = ["А", "Б", "В", "Г"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("10. Чья задача реагирование на оповещение о заражении антивирусом?\nА. Всех нижеперечисленных\nБ. Пользователь\nВ. Системный администратор\nГ. Администратор безопасности", reply_markup=keyboard)
        await IntroTestUser.q10.set()

@dp.message_handler(state=IntroTestUser.q10)
async def answer_q10(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == "А" or answer == "Б" or answer == "В" or answer == "Г":
        await state.update_data(q10=answer)
        data = await state.get_data()
        correct_answers = 0
        q1 = data.get("q1")
        q2 = data.get("q2")
        q3 = data.get("q3")
        q4 = data.get("q4")
        q5 = data.get("q5")
        q6 = data.get("q6")
        q7 = data.get("q7")
        q8 = data.get("q8")
        q9 = data.get("q9")
        q10 = data.get("q10")
        id = data.get("id")
        if q1 == "В":
            correct_answers+=1
        if q2 == "Б":
            correct_answers += 1
        if q3 == "В":
            correct_answers+=1
        if q4 == "А":
            correct_answers+=1
        if q5 == "А":
            correct_answers+=1
        if q6 == "Б":
            correct_answers+=1
        if q7 == "Б":
            correct_answers+=1
        if q8 == "Б":
            correct_answers+=1
        if q9 =="Б":
            correct_answers+=1
        if q10 =="А":
            correct_answers+=1

        if correct_answers >= 8:
            await sqlite_db.sql_update_intro_test_level(1, id)
        elif correct_answers < 8 and correct_answers>=4:
            await sqlite_db.sql_update_intro_test_level(2, id)
        else:
            await sqlite_db.sql_update_intro_test_level(3, id)

        db_row = await sqlite_db.sql_read(id)
        # await message.answer(str(db_row))
        explanation = ""
        if str(db_row[0][4])=="1":
            explanation = "У тебя уже есть довольно обширные знания в области кибербезопасности."
        elif str(db_row[0][4])=="2":
            explanation = "Твои знания по кибербезопасности пока на среднем уровне."
        elif str(db_row[0][4]) == "3":
            explanation = "У тебя пока не много знаний по кибербезопасности, но скоро мы это исправим."
        await message.answer("Поздравляем, ты закончил тест. По его результатам ты получил " + str(db_row[0][4]) + " уровень. "+explanation)
        video = open("dogs.mp4", 'rb')
        await bot.send_video((types.User.get_current()).id, video)
        await state.finish()

        start_buttons = ["Я готов 😎"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)
        await MainProgramGeneral.welcome.set()
        await message.answer("Теперь ты можешь перейти к основному блоку обучения. Когда будешь готов, нажми на кнопку!", reply_markup=keyboard)

