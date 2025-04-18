from aiogram import types

kb_start = [
    types.KeyboardButton(text='AddTask'),
    types.KeyboardButton(text='DeleteTask'),
    types.KeyboardButton(text='RewriteTask')
]

rw_task = [
    types.KeyboardButton(text='day'),
    types.KeyboardButton(text='time'),
    types.KeyboardButton(text='task'),
]