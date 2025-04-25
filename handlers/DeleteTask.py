from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types


from loader import router, con, cursor
from aiogram import F


class Form_delete(StatesGroup):
    number = State()


@router.message(F.text =='Удалить задачу')
async def fun_start(message: Message, state: FSMContext):
    cursor.execute('select * from zadacha')
    all = cursor.fetchall()
    await state.set_state((Form_delete.number))
    await message.answer(text=f'какую задачу вы хотите удалить?\n{all}',reply_markup=types.ReplyKeyboardRemove())


@router.message(Form_delete.number)
async def get_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    state1 = await state.get_data()
    number = state1['number']
    await state.clear()
    cursor.execute(f'delete from zadacha where id = {number}')
    cursor.execute('update zadacha set id = id-1 where id >= ?', (number))
    con.commit()
    await message.answer('задача удалена')