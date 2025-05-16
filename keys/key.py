from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from loader import router, con, cursor
from aiogram import F


kb_start = [
    types.KeyboardButton(text='Добавить задачу'),
    types.KeyboardButton(text='Удалить задачу'),
    types.KeyboardButton(text='Отредоктировать задачу')
]


rw_task = [
    types.KeyboardButton(text='День'),
    types.KeyboardButton(text='Время'),
    types.KeyboardButton(text='Описание')
]