from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import rw_task
from loader import router, con, cursor
from aiogram import F

import RW.t_rw
import RW
import RW
import RW
import RW
import RW
import RW

@router.message(F.text =='RewriteTask')
async def fun_start(message: Message):
    builder = ReplyKeyboardBuilder()
    for button in rw_task:
        builder.add(button)
    await message.answer(text='что иммено вы хотите отредоктировать?', reply_markup=builder.as_markup(resize_keyboard=True))