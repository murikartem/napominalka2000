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
    await state.set_state((Form_add.number))
    await message.answer(text=f'какую задачу вы хотите отредоктировать?\n{all}', reply_markup=types.ReplyKeyboardRemove())


@router.message(Form_add.number)
async def get_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    state1 = await state.get_data()
    number = state1['number']
    await state.clear()
    cursor.execute(f'select * from zadacha where id = {number}')
    data = cursor.fetchall()
    await message.answer('понел')
    builder = ReplyKeyboardBuilder()
    for button in rw_task:
        builder.add(button)
    await message.answer(text=f'что иммено вы хотите отредоктировать?\n{data[0]}', reply_markup=builder.as_markup(resize_keyboard=True))

    #time
    @router.message(F.text == 'время')
    async def time_rewrite(message: Message):
        cursor.execute(f'select time from zadacha where id = {number}')
        data1 = cursor.fetchall()
        await state.set_state((Form_add.newtime))
        await message.answer(text=f'выберите время которое вы хотите вместо: {data1[0][0]}', reply_markup=types.ReplyKeyboardRemove())

    @router.message(Form_add.newtime)
    async def get_newtime(message: Message, state: FSMContext):
        await state.update_data(newtime=message.text)
        state2 = await state.get_data()
        newtime = state2['newtime']
        cursor.execute(f'update zadacha set time=? where id=? ', (newtime, number))
        con.commit()
        await message.answer('время изменено')
        await state.clear()
    #day
    @router.message(F.text == 'день')
    async def day_rewrite(message: Message):
        cursor.execute(f'select day from zadacha where id = {number}')
        data2 = cursor.fetchall()
        await state.set_state((Form_add.newday))
        await message.answer(text=f'выберите день который вы хотите вместо: {data2[0][0]}',
                             reply_markup=types.ReplyKeyboardRemove())

    @router.message(Form_add.newday)
    async def get_newday(message: Message, state: FSMContext):
        await state.update_data(newday=message.text)
        state3 = await state.get_data()
        newday = state3['newday']
        cursor.execute(f'update zadacha set day=? where id=? ', (newday, number))
        con.commit()
        await message.answer('день изменён')
        await state.clear()
    #task
    @router.message(F.text == 'описание')
    async def task_rewrite(message: Message):
        cursor.execute(f'select task from zadacha where id = {number}')
        data3 = cursor.fetchall()
        await state.set_state((Form_add.newtask))
        await message.answer(text=f'выберите задачу которую вы хотите вместо: {data3[0][0]}',
                             reply_markup=types.ReplyKeyboardRemove())

    @router.message(Form_add.newtask)
    async def get_newtask(message: Message, state: FSMContext):
        await state.update_data(newtask=message.text)
        state4 = await state.get_data()
        newtask = state4['newtask']
        cursor.execute(f'update zadacha set task=? where id=? ', (newtask, number))
        con.commit()
        await message.answer('задача изменена')
        await state.clear()