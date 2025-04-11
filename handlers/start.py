from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router


@router.message(Command('start'))
async def start(message: Message):
    builder = ReplyKeyboardBuilder()

    await message.answer(text='Добро пожаловать!, чтоб продолжить введи команду tasks',
                         reply_markup=builder.as_markup(resize_keyboard=True))