import sqlite3
import asyncio
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.others import exam_kidoreld,exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, testing_menu_18_uzb, testing_menu_kid
from keyboards.inline.inline_KBs import lang
from keyboards.inline.tes import keyboard
from loader import dp, db, bot


@dp.message_handler(commands='start')
async def bot_start(message: types.Message,state:FSMContext):
    await state.set_state('Language')
    await message.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)

@dp.callback_query_handler(text='rus',state='Language')
async def russian_set_state(call:CallbackQuery, state:FSMContext):
    await state.set_state('Russian')
    await call.message.answer('Здраствуйте, напишите ваше полное имя имя:')

@dp.callback_query_handler(text='uzbek',state='Language')
async def russian_set_state(call: CallbackQuery, state: FSMContext):
    await state.set_state('Uzbek')
    await call.message.answer("Assalomu Aleykum, to'liq ismingizni yozing:")

@dp.message_handler(state='Russian')
async def registration_name(msg: types.Message):
    await msg.answer('Какой тест вы проходите\n!!!ВЫ НЕ СМОЖЕТЕ ИЗМЕНИТЬ ЭТО ПОТОМ!!!:', reply_markup=exam_kidoreld)
    name = msg.text
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    language='ru')
    except sqlite3.InternalError as err:
        print(err)

@dp.message_handler(state='Uzbek')
async def registration_name_uzb(msg: types.Message):
    await msg.answer("Qanaqa test o'tayabsiz:\n!!!JAVOBINGIZNI O'ZGARTIROLMAYSIZ!!!", reply_markup=exam_kidoreld_uzb)
    name = msg.text
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    language='uz')
    except sqlite3.InternalError as err:
        print(err)

@dp.callback_query_handler(state='Russian',text='kid')
async def rus_kid(call:CallbackQuery):
    await call.message.answer('Выберите тест',reply_markup=testing_menu_kid)

@dp.callback_query_handler(state='Russian',text='18+')
async def rus_kid(call:CallbackQuery):
    await call.message.answer('Выберите тест:',reply_markup=testing_menu_18)

@dp.callback_query_handler(state='Uzbek',text='kid_uzb')
async def rus_kid(call:CallbackQuery):
    await call.message.answer('Test tanlang:',reply_markup=testing_menu_kid_uzb)

@dp.callback_query_handler(state='Uzbek',text='18+_uzb')
async def rus_kid(call:CallbackQuery):
    await call.message.answer('Test tanlang:',reply_markup=testing_menu_18_uzb)
