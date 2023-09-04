from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.inline_KBs import lang
from loader import dp

@dp.callback_query_handler(text='lang' ,state=['Russian','Uzbek'])
async def set_state(call:CallbackQuery, state: FSMContext):
    await call.message.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
    await state.set_state('Language')

@dp.message_handler(commands='lang',state=['Russian','Uzbek'])
async def set_state(msg: types.Message, state: FSMContext):
    await msg.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)
    await state.set_state('Language')

