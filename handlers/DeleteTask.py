from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types


from loader import router, con, cursor
from aiogram import F

#@router.message(F.text =='DeleteTask')
#async def fun_start(message: Message, state: FSMContext):