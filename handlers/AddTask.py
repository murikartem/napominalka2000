from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types


from loader import router, con, cursor
from aiogram import F

class Form_add(StatesGroup):
    day = State()
    time = State()
    task = State()


@router.message(F.text =='AddTask')
async def fun_start(message: Message, state: FSMContext):

    await state.set_state((Form_add.day))
    await message.answer(text='введите день для события!',reply_markup=types.ReplyKeyboardRemove())




@router.message(Form_add.day)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(day=message.text)
    await state.set_state(Form_add.time)
    await message.answer('а теперь введи время события')

@router.message(Form_add.time)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Form_add.task)
    await message.answer('а теперь введи само событие')


@router.message(Form_add.task)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    data1 = await state.get_data()
    day = data1['day']
    time = data1['time']
    task = data1['task']
    await state.clear()
    cursor.execute('insert into zadacha (day, task, time) values (?,?,?)', [day, task, time])
    con.commit()
    await message.answer('задача сохранена')