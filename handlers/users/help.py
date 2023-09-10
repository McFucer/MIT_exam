from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.menu_after_tests import iq_test_after_english
from keyboards.inline.others import exam_kidoreld,exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, testing_menu_18_uzb, testing_menu_kid
from keyboards.inline.inline_KBs import lang,  markup_cont
from keyboards.inline.iq_test import quest1, quest2, quest3, quest4, quest5, quest10, quest6, quest7, quest8, quest9, \
    quest11, quest12, quest13, quest14, quest15, quest16, quest17, quest18, quest19, quest20, quest21, quest22, quest23, \
    quest24, quest25
from loader import dp, db, bot

@dp.callback_query_handler(text='englishtest_after',state='*')
async def choose(call:CallbackQuery):
    await call.message.answer("Какой тест вы проходите? | Qanaqa test o'tayabsiz",reply_markup=assure_4_test)