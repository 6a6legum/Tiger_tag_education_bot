from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from states.main_program import MainProgramGeneral
from loader import dp, bot
from data_base import sqlite_db
import random
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink


def random_correct_gifs():
    texts = ["ok1.mp4", "ok2.mp4", "ok3.mp4", "ok4.mp4"]
    i = random.randint(0, 3)
    return texts[i]



def random_wrong_gifs():
    texts = ["bad1.mp4", "bad2.mp4", "bad3.mp4", "bad4.mp4"]
    i = random.randint(0, 3)
    return texts[i]

def random_thinking_gifs():
    texts = ["q1.mp4", "q2.mp4", "q3.mp4", "q4.mp4", "q5.mp4"]
    i = random.randint(0, 4)
    return texts[i]

@dp.message_handler(text="Поехали 🚑", state=MainProgramGeneral.lesson_welcome_user)
async def start_lesson(message: types.Message,  state: FSMContext):
    await message.answer("У нас есть выделенная полоса для движения спецтранспорта, но нам необходимо как-то проверять чтобы туда заезжал исключительно он.")
    await message.answer("Как мы будем решать эту задачу на примере Microsoft Office?")
    video_name = random_thinking_gifs()
    video = open(video_name, 'rb')
    await bot.send_video((types.User.get_current()).id, video)

    await message.answer(f"{hbold('Добавление невидимых цифровых подписей в документ Word, Excel или PowerPoint!!')}\n")
    photo = open("security.png", 'rb')
    await bot.send_photo((types.User.get_current()).id, photo)
    await message.answer("Чтобы удостоверить подлинность содержимого документа, можно добавить в него невидимую цифровую подпись. В нижней части подписанных документов будет находиться кнопка Подписи.")
    await message.answer("Что для этого нужно сделать?")
    await message.answer("1️⃣Откройте вкладку Файл.\n\n2️⃣Выберите пункт Сведения.\n\n3️⃣Нажмите кнопку Защита документа, Защита книги или Защита презентации.\n\n4️⃣Нажмите кнопку Добавить цифровую подпись."
                         + "\n\n5️⃣Прочитайте сообщение Word, Excel или PowerPoint и нажмите кнопку ОК.\n\n6️⃣В диалоговом окне Подпись в поле Цель подписания документа укажите цель подписания документа\n\n7️⃣Щелкните элемент Подпись.")
    await message.answer("После того как в файл будет добавлена цифровая подпись, появится кнопка Подписи, а сам файл станет доступен только для чтения.")

    video_name1 = random_correct_gifs()
    video1 = open(video_name1, 'rb')
    await bot.send_video((types.User.get_current()).id, video1)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Вернуться на главную⬅"),
            ],
            [
                KeyboardButton(text="Ещё теории!"),
            ],

        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Ты прошёл один урок. Что будешь делать дальше?", reply_markup=keyboard)
    await MainProgramGeneral.lesson_q1_user.set()


@dp.message_handler(text="Ещё теории!", state=MainProgramGeneral.lesson_q1_user)
async def start_lesson(message: types.Message,  state: FSMContext):

        # video = open(video_name, 'rb')
        # await bot.send_video((types.User.get_current()).id, video)
        await message.answer("Сейчас мы рассмотрим...")
        await message.answer(f"{hbold('Безопасный интернет серфинг')}\n")
        video = open("surf.mp4", 'rb')
        await bot.send_video((types.User.get_current()).id, video)
        await message.answer("Почему это важно?")

        await message.answer("Интернет стал неотъемлемой частью нашей жизни, а веб-браузеры стали нашими воротами к информации. Знание того, как определять вредоносные ссылки и веб-сайты, может иметь значение, если вас взломают или нет.")

        start_buttons = ["Да", "Нет"]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer("А ты когда-нибудь задумывался как отличить поддельные сайты от настоящих?", reply_markup=keyboard)
        await MainProgramGeneral.lesson_q2_user.set()
        # start_buttons = ["Вернуться на главную⬅"]
        # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        # keyboard.add(*start_buttons)
        # await message.answer("Ты изучил все вопросы, которые есть на данный момент. Возвращайся позднее, здесь обязательно появится что-нибудь новое", reply_markup=keyboard)

@dp.message_handler(text="Да", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message,  state: FSMContext):

        # video = open(video_name, 'rb')
        # await bot.send_video((types.User.get_current()).id, video)
        await message.answer("Круто! Но повторить не помешало бы, правда?")

        await state.update_data(button_clicked=0)
        await state.update_data(pwd_scam=0)
        await state.update_data(window_scam=0)
        await state.update_data(bank_scam=0)
        await state.update_data(conv_scam=0)

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Мошенничество с паролем"),
                ],
                [
                    KeyboardButton(text="Мошенничество с окнами"),
                ],
                [
                    KeyboardButton(text="Банковское дело"),
                ],
                [
                    KeyboardButton(text="Исключительное предложение"),
                ],
            ],
            resize_keyboard=True
        )
        await message.answer(
            "Веб-сайты можно настроить за считанные минуты, и хакеры всегда ищут новые способы получить вашу личную информацию. Вот некоторые из этих распространенных тактик.", reply_markup=keyboard)
        await MainProgramGeneral.lesson_q2_user.set()


@dp.message_handler(text="Нет", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)
    await message.answer("Ничего страшного, сейчас ты про это узнаешь.")

    await state.update_data(button_clicked=0)
    await state.update_data(pwd_scam=0)
    await state.update_data(window_scam=0)
    await state.update_data(bank_scam=0)
    await state.update_data(conv_scam=0)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Мошенничество с паролем"),
            ],
            [
                KeyboardButton(text="Мошенничество с окнами"),
            ],
            [
                KeyboardButton(text="Банковское дело"),
            ],
            [
                KeyboardButton(text="Исключительное предложение"),
            ],
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Веб-сайты можно настроить за считанные минуты, и хакеры всегда ищут новые способы получить вашу личную информацию. Вот некоторые из этих распространенных тактик.",
        reply_markup=keyboard)
    await MainProgramGeneral.lesson_q2_user.set()


@dp.message_handler(text="Мошенничество с паролем", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)


    async with state.proxy() as data:
        data["button_clicked"]+=1
        data["pwd_scam"] += 1

    data = await state.get_data()
    window_scam = data.get("window_scam")
    bank_scam = data.get("bank_scam")
    conv_scam = data.get("conv_scam")
    if window_scam==0 and bank_scam==0 and conv_scam==0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"),],
                [KeyboardButton(text="Банковское дело"),],
                [KeyboardButton(text="Исключительное предложение"),],], resize_keyboard=True)
    elif window_scam==0 and bank_scam==0 and conv_scam==1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
                [KeyboardButton(text="Банковское дело"), ],
                ], resize_keyboard=True)
    elif window_scam == 0 and bank_scam == 1 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and bank_scam ==0 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and bank_scam ==1 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and bank_scam == 0 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
            ], resize_keyboard=True)
    elif window_scam == 0 and bank_scam == 1 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and bank_scam == 1 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Дальше➡"), ],
            ], resize_keyboard=True)


    await message.answer("Поддельное электронное письмо с требованием сбросить или подтвердить пароль учетной записи. После ввода ваш пароль будет отправлен непосредственно хакеру.", reply_markup=keyboard)
    await MainProgramGeneral.lesson_q2_user.set()


@dp.message_handler(text="Банковское дело", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)


    async with state.proxy() as data:
        data["button_clicked"] += 1
        data["bank_scam"] += 1

    data = await state.get_data()
    window_scam = data.get("window_scam")
    pwd_scam = data.get("pwd_scam")
    conv_scam = data.get("conv_scam")
    if window_scam == 0 and pwd_scam == 0 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
                [KeyboardButton(text="Мошенничество с паролем"), ],
                [KeyboardButton(text="Исключительное предложение"), ], ], resize_keyboard=True)
    elif window_scam == 0 and pwd_scam == 0 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
                [KeyboardButton(text="Мошенничество с паролем"), ],
            ], resize_keyboard=True)
    elif window_scam == 0 and pwd_scam == 1 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and pwd_scam == 0 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с паролем"), ],
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and pwd_scam == 1 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and pwd_scam == 0 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с паролем"), ],
            ], resize_keyboard=True)
    elif window_scam == 0 and pwd_scam == 1 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
            ], resize_keyboard=True)
    elif window_scam == 1 and pwd_scam == 1 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Дальше➡"), ],
            ], resize_keyboard=True)

    await message.answer(
        "Эти мошеннические банковские веб-сайты, выглядящие как настоящие, собирают информацию о вашей учетной записи и отправляют ее непосредственно хакеру.",
        reply_markup=keyboard)
    await MainProgramGeneral.lesson_q2_user.set()

@dp.message_handler(text="Мошенничество с окнами", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)


    async with state.proxy() as data:
        data["button_clicked"] += 1
        data["window_scam"] += 1
    data = await state.get_data()
    bank_scam = data.get("bank_scam")
    pwd_scam = data.get("pwd_scam")
    conv_scam = data.get("conv_scam")
    if bank_scam == 0 and pwd_scam == 0 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
                [KeyboardButton(text="Мошенничество с паролем"), ],
                [KeyboardButton(text="Исключительное предложение"), ], ], resize_keyboard=True)
    elif bank_scam == 0 and pwd_scam == 0 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
                [KeyboardButton(text="Мошенничество с паролем"), ],
            ], resize_keyboard=True)
    elif bank_scam == 0 and pwd_scam == 1 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 0 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с паролем"), ],
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 1 and conv_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Исключительное предложение"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 0 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с паролем"), ],
            ], resize_keyboard=True)
    elif bank_scam == 0 and pwd_scam == 1 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 1 and conv_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Дальше➡"), ],
            ], resize_keyboard=True)

    await message.answer(
        "Всплывающее окно с сообщением о том, что на вашем компьютере обнаружено вредоносное ПО, сопровождается предложением бесплатно просканировать ваш компьютер.",
        reply_markup=keyboard)
    await MainProgramGeneral.lesson_q2_user.set()

@dp.message_handler(text="Исключительное предложение", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)


    async with state.proxy() as data:
        data["button_clicked"] += 1
        data["conv_scam"] += 1

    data = await state.get_data()
    bank_scam = data.get("bank_scam")
    pwd_scam = data.get("pwd_scam")
    window_scam = data.get("window_scam")
    if bank_scam == 0 and pwd_scam == 0 and window_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
                [KeyboardButton(text="Мошенничество с паролем"), ],
                [KeyboardButton(text="Мошенничество с окнами"), ], ], resize_keyboard=True)
    elif bank_scam == 0 and pwd_scam == 0 and window_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
                [KeyboardButton(text="Мошенничество с паролем"), ],
            ], resize_keyboard=True)
    elif bank_scam == 0 and pwd_scam == 1 and window_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
                [KeyboardButton(text="Мошенничество с окнами"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 0 and window_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с паролем"), ],
                [KeyboardButton(text="Мошенничество с окнами"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 1 and window_scam == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с окнами"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 0 and window_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мошенничество с паролем"), ],
            ], resize_keyboard=True)
    elif bank_scam == 0 and pwd_scam == 1 and window_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Банковское дело"), ],
            ], resize_keyboard=True)
    elif bank_scam == 1 and pwd_scam == 1 and window_scam == 1:
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Дальше➡"), ],
            ], resize_keyboard=True)

    await message.answer(
        "Эти онлайн-мошенники утверждают, что вы выиграли приз, а затем просят вас ввести свою личную информацию, чтобы воспользоваться фальшивым предложением.",
        reply_markup=keyboard)
    await MainProgramGeneral.lesson_q2_user.set()

@dp.message_handler(text="Дальше➡", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)
    await message.answer("На что же обращать внимание?")
    await  message.answer("Хотя конкретные детали мошеннических веб-сайтов могут отличаться, вот некоторые из наиболее распространенных вещей, на которые следует обращать внимание.")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Погнали дальше🚕"), ],
            ], resize_keyboard=True, one_time_keyboard=True)


    await message.answer(
        "1️⃣ Чувство срочности\n\nУгрозы, страх и чувство срочности - все это распространенные тактики, которые хакеры используют, чтобы обмануть своих жертв, заставляя сначала действовать, а думать потом.\n\n" +
        "2️⃣ Отсутствует поиск\n\nВсегда ищите значок замка, также известный как HTTPS, на панели браузера. Это означает, что веб-сайт безопасен, а ваша конфиденциальная информация зашифрована.\n\n" +
        "3️⃣ Странная ссылка\n\nВсегда перепроверяйте URL-адрес веб-сайта на предмет нарушений. В случае сомнений введите URL вручную или используйте общедоступные ресурсы.\n\nВредоносная реклама\n\n" +
        "Вредоносная реклама - это использование интернет-рекламы для распространения вредоносного ПО, которую можно даже найти на законных веб-сайтах. Остерегайтесь «специальных предложений», которые могут привести к вредоносным веб-сайтам и даже заразить ваш компьютер программами-вымогателями.",
        reply_markup=keyboard)
    await MainProgramGeneral.lesson_q2_user.set()

@dp.message_handler(text="Погнали дальше🚕", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)
    await message.answer("Несколько советов для безопасности")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Поехали дальше🚕"), ],
            ], resize_keyboard=True, one_time_keyboard=True)


    await message.answer(
        "1️⃣ Проверьте свое окружение\n\nПри посещении веб-сайтов всегда ищите нечетные URL-адреса, отсутствующие значки блокировки или любые орфографические ошибки на странице.\n\n" +
        "2️⃣ Оставайтесь в курсе\n\nПостоянное обновление вашего браузера и другого программного обеспечения с помощью последних исправлений безопасности поможет защитить вас от широкого спектра интернет-угроз.\n\n" +
        "3️⃣ Не нажимайте\n\nХакерский дизайн предлагает ссылки, чтобы они были как можно более заманчивыми, но когда что-то кажется слишком хорошим, чтобы быть правдой, это обычно так.",
        reply_markup=keyboard)
    await MainProgramGeneral.lesson_q2_user.set()

@dp.message_handler(text="Поехали дальше🚕", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message, state: FSMContext):
    # video = open(video_name, 'rb')
    # await bot.send_video((types.User.get_current()).id, video)
    await message.answer(f"{hbold('Не забывай про свою роль!')}\n")

    await message.answer(
        "Интернет - большая часть нашей жизни, но он также открывает вам и вашей организации киберугрозы. Безопасная работа в Интернете - важнейший навык, который со временем развивается. Используйте методы, которые вы узнали сегодня, для дальнейшего развития этого навыка.")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Вернуться на главную⬅"),
            ],
            [
                KeyboardButton(text="Ещё теории!!"),
            ],

        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Ты прошёл урок. Что будешь делать дальше?", reply_markup=keyboard)


@dp.message_handler(text="Ещё теории!!", state=MainProgramGeneral.lesson_q2_user)
async def start_lesson(message: types.Message,  state: FSMContext):
    start_buttons = ["Вернуться на главную⬅"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Ты изучил все вопросы, которые есть на данный момент. Возвращайся позднее, здесь обязательно появится что-нибудь новое", reply_markup=keyboard)