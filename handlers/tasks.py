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
    for button in kb_start:
        builder.add(button)
    await message.answer(text=f'вот весь список ваших задач:{all}')
    await message.answer(text='Чего желаете?',
                         reply_markup=builder.as_markup(resize_keyboard=True))