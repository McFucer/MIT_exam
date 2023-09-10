from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


exam_kidoreld = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Для детей(1-14)', callback_data='kid')
    ],
    [
        InlineKeyboardButton(text='Для взрослых(15+)', callback_data='18+')
    ]

])

exam_kidoreld_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Bolalarniki', callback_data='kid_uzb')
    ],
    [
        InlineKeyboardButton(text='Kattalarniki', callback_data='18+_uzb')
    ]

])

testing_menu_kid = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Тест по английскому', callback_data='english_test_kid')
    ],
    [
        InlineKeyboardButton(text='Тест на IQ', callback_data='iq_test')
    ],
])

testing_menu_18 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Тест по английскому', callback_data='english_test')
    ],
    [
        InlineKeyboardButton(text='Тест на IQ', callback_data='iq_test')
    ],
])

testing_menu_kid_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ingliz tili testi", callback_data='english_test_kid')
    ],
    [
        InlineKeyboardButton(text='IQ testi', callback_data='iq_test')
    ],
])

testing_menu_18_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Ingliz tili testi', callback_data='english_test')
    ],
    [
        InlineKeyboardButton(text='IQ testi', callback_data='iq_test')
    ],
])
