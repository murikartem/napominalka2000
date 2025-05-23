from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router, con, cursor


@router.message(Command('tasks'))
async def task_start(message: Message):
    builder = ReplyKeyboardBuilder()
    cursor.execute('select * from zadacha')
    all = cursor.fetchall()
    text = ''
    for task in all:
        text += f'{task[1]}, {task[2]}, {task[3]}\n'
    for button in kb_start:
        builder.add(button)
    await message.answer(text=f'Вот весь список ваших задач:\n\n{text}\nЧего желаете?',reply_markup=builder.as_markup(resize_keyboard=True))
