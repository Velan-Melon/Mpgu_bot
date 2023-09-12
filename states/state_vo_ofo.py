from aiogram.dispatcher.filters.state import StatesGroup, State

class vo11_ofo(StatesGroup):
    vo11_ofo_step_start = State()
    vo11_ofo_step_0 = State()
    vo11_ofo_step_1 = State()
    vo11_ofo_step_2 = State()
    vo11_ofo_step_3 = State()
    vo11_ofo_step_4 = State()
    vo11_ofo_step_5 = State()
    vo11_ofo_step_6 = State()
    vo11_ofo_step_7 = State()
    vo11_ofo_step_finish = State()


class vo_spo_ofo(StatesGroup):
    vo_spo_ofo_step_0 = State()
    vo_spo_ofo_step_1 = State()
    vo_spo_ofo_step_2 = State()
    vo_spo_ofo_step_3 = State()
    vo_spo_ofo_step_4 = State()
    vo_spo_ofo_step_5 = State()
    vo_spo_ofo_step_6 = State()
    vo_spo_ofo_step_7 = State()
    vo_spo_ofo_step_finish = State()


class vo_vo_ofo(StatesGroup):
    vo_vo_ofo_step_0 = State()
    vo_vo_ofo_step_1 = State()
    vo_vo_ofo_step_2 = State()
    vo_vo_ofo_step_3 = State()
    vo_vo_ofo_step_4 = State()
    vo_vo_ofo_step_5 = State()
    vo_vo_ofo_step_6 = State()
    vo_vo_ofo_step_7 = State()
    vo_vo_ofo_step_finish = State()
