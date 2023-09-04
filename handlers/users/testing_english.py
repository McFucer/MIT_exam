import sqlite3
import asyncio
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.others import exam_kidoreld,exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, testing_menu_18_uzb, testing_menu_kid
from keyboards.inline.inline_KBs import lang, quest1
from keyboards.inline.tes import keyboard
from loader import dp, db, bot
points = 0


@dp.callback_query_handler(text='english_test_kid',state='Russian')
async def EnglishTest_kid(call:CallbackQuery, state:FSMContext):
    await state.set_state('english_test_kid')
    await call.message.answer('''1/60
I ______ bus on Mondays.
a.'m going to work with
b.'m going to work by
c.go to work with
d.go to work by''',reply_markup = quest1)

@dp.callback_query_handler(lambda c: c.data,state="english_test_kid")
async def q1(call:CallbackQuery):
    points = 0
    if call.data == 'a1':
        points = 1
