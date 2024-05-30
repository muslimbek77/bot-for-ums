from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()

class UMS(StatesGroup): 
    ums = State()
    location = State()

