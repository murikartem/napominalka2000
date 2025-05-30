from aiogram import types


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