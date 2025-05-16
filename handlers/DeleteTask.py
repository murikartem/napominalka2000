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

        text2.append(types.InlineKeyboardButton(text=f'{task[0]}. {task[1]}, {task[2]}, {task[3]}', callback_data=f'del_{task[0]}'))
    builder = InlineKeyboardBuilder()

    for button in text2:
        builder.add(button)
        builder.adjust(1)

    await message.answer(text=f'Какую задачу вы хотите удалить?\n\n{text}',reply_markup=builder.as_markup())




@router.message(Form_delete.number)
async def get_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    state1 = await state.get_data()
    number = state1['number']
    await state.clear()
    cursor.execute(f'delete from zadacha where id = {number}')
    cursor.execute('update zadacha set id = id-1 where id >= ?', (number))
    con.commit()
    await message.answer('Задача удалена, если хотите зделать что-то еще введите команду-/tasks')