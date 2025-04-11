from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router, con, cursor
from aiogram import F

@router.message(F.text =='time')
async def time_rewrite(message: Message):
    builder = ReplyKeyboardBuilder()
    cursor.execute('select time from zadacha')
    data = cursor.fetchall()
    await message.answer(text=f'что иммено вы хотите {data}', reply_markup=builder.as_markup(resize_keyboard=True))