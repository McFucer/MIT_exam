import sqlite3
import asyncio
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.others import exam_kidoreld,exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, testing_menu_18_uzb, testing_menu_kid
from keyboards.inline.inline_KBs import lang
from loader import dp, db, bot


@dp.message_handler()
async def handler(msg:types.Message):
    await msg.delete()