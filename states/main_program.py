from aiogram.dispatcher.filters.state import StatesGroup, State


class MainProgramGeneral(StatesGroup):
    welcome = State()
    waitingForAnswer = State()
    quiz_welcome_user = State()
    quiz_q1_user = State()
    quiz_q2_user = State()
    quiz_q3_user = State()

    quiz_welcome_operator = State()
    quiz_q1_operator = State()
    quiz_q2_operator = State()
    quiz_q3_operator = State()

    quiz_welcome_admin = State()
    quiz_q1_admin = State()
    quiz_q2_admin = State()
    quiz_q3_admin = State()

    lesson_welcome_user = State()
    lesson_q1_user = State()
    lesson_q2_user = State()
    lesson_q3_user = State()

    lesson_welcome_operator = State()
    lesson_q1_operator = State()
    lesson_q2_operator = State()
    lesson_q3_operator = State()

    lesson_welcome_admin = State()
    lesson_q1_admin = State()
    lesson_q2_admin = State()
    lesson_q3_admin = State()

    cases_welcome_user = State()
    cases_q1_user = State()
    cases_q2_user = State()
    cases_q3_user = State()

    cases_welcome_operator = State()
    cases_q1_operator = State()
    cases_q2_operator = State()
    cases_q3_operator = State()

    cases_welcome_admin = State()
    cases_q1_admin = State()
    cases_q2_admin = State()
    cases_q3_admin = State()
