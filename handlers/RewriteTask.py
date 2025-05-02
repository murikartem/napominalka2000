from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import rw_task
from loader import router, con, cursor
from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram import types
from aiogram.fsm.context import FSMContext


class Form_add(StatesGroup):
    number = State()
    newtime = State()
    newday = State()
    newtask = State()

@router.message(F.text =='Отредоктировать задачу')
async def fun_start(message: Message, state: FSMContext):
    cursor.execute('select * from zadacha')
    all = cursor.fetchall()
    text = ''
    for task in all:
        text += f'{task[0]}. {task[1]}, {task[2]}, {task[3]}\n'
    await state.set_state((Form_add.number))
    await message.answer(text=f'Какую задачу вы хотите отредоктировать?\n\n{text}', reply_markup=types.ReplyKeyboardRemove())


@router.message(Form_add.number)
async def get_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    state1 = await state.get_data()
    number = state1['number']
    await state.clear()
    cursor.execute(f'select * from zadacha where id = {number}')
    data = cursor.fetchall()
    await message.answer('Понял')
    builder = ReplyKeyboardBuilder()
    for button in rw_task:
        builder.add(button)
    await message.answer(text=f'{data[0][1]}, {data[0][2]}, {data[0][3]}\n\nЧто иммено вы хотите отредоктировать?', reply_markup=builder.as_markup(resize_keyboard=True))

    #time
    @router.message(F.text == 'Время')
    async def time_rewrite(message: Message):
        cursor.execute(f'select time from zadacha where id = {number}')
        data1 = cursor.fetchall()
        await state.set_state((Form_add.newtime))
        await message.answer(text=f'Выберите время которое вы хотите вместо: {data1[0][0]}', reply_markup=types.ReplyKeyboardRemove())

    @router.message(Form_add.newtime)
    async def get_newtime(message: Message, state: FSMContext):
        await state.update_data(newtime=message.text)
        state2 = await state.get_data()
        newtime = state2['newtime']
        cursor.execute(f'update zadacha set time=? where id=? ', (newtime, number))
        con.commit()
        await message.answer('Время изменено, если хотите зделать что-то еще введите команду-/tasks')
        await state.clear()
    #day
    @router.message(F.text == 'День')
    async def day_rewrite(message: Message):
        cursor.execute(f'select day from zadacha where id = {number}')
        data2 = cursor.fetchall()
        await state.set_state((Form_add.newday))
        await message.answer(text=f'Выберите день который вы хотите вместо: {data2[0][0]}',
                             reply_markup=types.ReplyKeyboardRemove())

    @router.message(Form_add.newday)
    async def get_newday(message: Message, state: FSMContext):
        await state.update_data(newday=message.text)
        state3 = await state.get_data()
        newday = state3['newday']
        cursor.execute(f'update zadacha set day=? where id=? ', (newday, number))
        con.commit()
        await message.answer('День изменён, если хотите зделать что-то еще введите команду-/tasks')
        await state.clear()
    #task
    @router.message(F.text == 'Описание')
    async def task_rewrite(message: Message):
        cursor.execute(f'select task from zadacha where id = {number}')
        data3 = cursor.fetchall()
        await state.set_state((Form_add.newtask))
        await message.answer(text=f'Выберите задачу которую вы хотите вместо: {data3[0][0]}',
                             reply_markup=types.ReplyKeyboardRemove())

    @router.message(Form_add.newtask)
    async def get_newtask(message: Message, state: FSMContext):
        await state.update_data(newtask=message.text)
        state4 = await state.get_data()
        newtask = state4['newtask']
        cursor.execute(f'update zadacha set task=? where id=? ', (newtask, number))
        con.commit()
        await message.answer('Задача изменена, если хотите зделать что-то еще введите команду-/tasks')
        await state.clear()