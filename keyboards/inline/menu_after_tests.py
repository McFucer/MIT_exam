from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


menu_after_english = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text='Iq test',callback_data='iqtest_after_english')
    ]
])

iq_test_after_english = InlineKeyboardMarkup(
inline_keyboard=[
    [
InlineKeyboardButton(text='English_test',callback_data='englishtest_after'),
    ]
])

assure_4_test = InlineKeyboardMarkup(
    inline_keyboard=[
    [
InlineKeyboardButton(text='Bolalarniki | Детский',callback_data='kid_re'),
InlineKeyboardButton(text='Kattalarniki | Взрослый',callback_data='eld_re'),
    ]

])