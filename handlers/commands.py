from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router, con, cursor


@router.message(Command('help'))
async def help(message: Message):
    builder = ReplyKeyboardBuilder()
    await message.answer(text='Вот список все команнды на данный момент:\n/start\n/tasks\n/help\n/Del-all',
                         reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(Command('Dell-all'))
async def start(message: Message):
    cursor.execute(f'delete from zadacha')
    con.commit()
    await message.answer('Все задачи удалены, если хотите зделать создать новую введите команду-/tasks')