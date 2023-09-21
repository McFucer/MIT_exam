import sqlite3
import asyncio
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.others import exam_kidoreld,exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, testing_menu_18_uzb, testing_menu_kid
from keyboards.inline.inline_KBs import lang

from loader import dp, db, bot
from test import timer_callback


@dp.message_handler(commands='start')
async def bot_start(message: types.Message,state:FSMContext):
    await message.delete()
    await state.set_state('Language')
    await message.answer("Выберите язык:\nTil tanlang:", reply_markup=lang)

@dp.callback_query_handler(text='rus',state='Language')
async def russian_set_state(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await state.set_state('Russian')
    await call.message.answer('Здраствуйте, напишите ваше полное имя имя:')

@dp.callback_query_handler(text='uzbek',state='Language')
async def russian_set_state(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.set_state('Uzbek')
    await call.message.answer("Assalomu Aleykum, to'liq ismingizni yozing:")

@dp.message_handler(state='Russian')
async def registration_name(msg: types.Message):
    await msg.delete()
    await msg.answer('Какой тест вы проходите\nКак только вы выберите тест у вас начнется таймер на 30 минут. Мы будем оповещать вас каждые 10 минут.\n!!!ВЫ НЕ СМОЖЕТЕ ИЗМЕНИТЬ ЭТО ПОТОМ!!!:', reply_markup=exam_kidoreld)
    name = msg.text
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    language='ru')
    except sqlite3.InternalError as err:
        print(err)

@dp.message_handler(state='Uzbek')
async def registration_name_uzb(msg: types.Message):
    await msg.delete()
    await msg.answer("Qanaqa test o'tayabsiz:\nTestni tanlashingiz bilanoq taymer 30 daqiqaga ishga tushadi. Sizga har 10 daqiqada xabar beramiz.\n!!!JAVOBINGIZNI O'ZGARTIROLMAYSIZ!!!", reply_markup=exam_kidoreld_uzb)
    name = msg.text
    try:
        db.add_user(id=msg.from_user.id,
                    name=name,
                    language='uz')
    except sqlite3.InternalError as err:
        print(err)

@dp.callback_query_handler(text='kid',state='*')
async def dcac(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer('Начать тест\n<b>Тест по английскому: 40 вопросов</b>',reply_markup=testing_menu_kid)
    await asyncio.create_task(timer_callback(call.message, state))


@dp.callback_query_handler(text='18+',state='*')
async def dcscvrs(call:CallbackQuery, state:FSMContext):
    await call.message.delete()

    await call.message.answer('Начать тест:\n<b>Тест по английскому: 60 вопросов</b>',reply_markup=testing_menu_18)
    await asyncio.create_task(timer_callback(call.message, state))

@dp.callback_query_handler(text='kid_uzb',state='*')
async def vsvsvfs(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer('Test boshlash:\n<b>Ingliz tili testi: 40 savol</b>',reply_markup=testing_menu_kid_uzb)
    await asyncio.create_task(timer_callback(call.message, state))


@dp.callback_query_handler(text='18+_uzb', state='*')
async def vsfvfbsb(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    await call.message.answer('Test boshlash:\n<b>Ingliz tili testi: 60 savol</b>', reply_markup=testing_menu_18_uzb)
    await asyncio.create_task(timer_callback(call.message, state))