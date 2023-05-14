from aiogram.fsm.state import StatesGroup, State


class WorkState(StatesGroup):
    material = State()
    size = State()
    complexity = State()
    color = State()
    decoration = State()
    discount = State()
    offer = State()
    final = State()