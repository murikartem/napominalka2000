from aiogram import types

kb_start = [
    types.KeyboardButton(text='AddTask'),
    types.KeyboardButton(text='DeleteTask'),
    types.KeyboardButton(text='RewriteTask')
]

rw_task = [
    types.KeyboardButton(text='day'),
    types.KeyboardButton(text='day-time'),
    types.KeyboardButton(text='time'),
    types.KeyboardButton(text='time-task'),
    types.KeyboardButton(text='task'),
    types.KeyboardButton(text='day-task'),
    types.KeyboardButton(text='all'),
]