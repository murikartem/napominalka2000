from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


from loader import router, con, cursor
from aiogram import F


class Form_delete(StatesGroup):
    number = State()


@router.message(F.text =='Удалить задачу')
async def fun_start(message: Message):
    cursor.execute('select * from zadacha')
    all = cursor.fetchall()
    text = ''
    text2 = []
    for task in all:

        text2.append(types.InlineKeyboardButton(text=f'{task[1]}, {task[2]}, {task[3]}', callback_data=f'bet_{task[0]}'))
    builder = InlineKeyboardBuilder()

    for button in text2:
        builder.add(button)
        builder.adjust(1)

    await message.answer(text=f'Какую задачу вы хотите удалить?\nчтобы зделать что-то еще введите команду-/tasks\n{text}',reply_markup=builder.as_markup())




@router.callback_query(F.data.startswith('bet'))
async def delete(callback: types.CallbackQuery, bot):
    bet = int(callback.data.split('_')[1])
    cursor.execute(f'delete from zadacha where id = {bet}')
    con.commit()
    await callback.answer('Задача удалена')