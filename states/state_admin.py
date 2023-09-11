from aiogram.dispatcher.filters.state import StatesGroup, State

class admin(StatesGroup):
    adm_step_1 = State()
    adm_step_2 = State()
    adm_step_3 = State()
    adm_step_4 = State()
    adm_step_5 = State()
    adm_step_6 = State()
class admin_delete_state(StatesGroup):
    adm_delete_1 = State
    adm_delete_2 = State
    adm_delete_3 = State

