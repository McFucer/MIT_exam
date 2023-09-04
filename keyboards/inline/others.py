from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


exam_kidoreld = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Детский', callback_data='kid')
    ],
    [
        InlineKeyboardButton(text='Дедский', callback_data='18+')
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
        InlineKeyboardButton(text='Тест на IQ', callback_data='iq_test_kid')
    ],
    [
        InlineKeyboardButton(text='Тест на логическое мышление', callback_data='logic_test_kid')
    ],
    [
        InlineKeyboardButton(text="Tilni o'zgartirish", callback_data='lang')
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
    [
        InlineKeyboardButton(text='Тест на логическое мышление', callback_data='logic_test')
    ],
    [
        InlineKeyboardButton(text="Tilni o'zgartirish", callback_data='lang')
    ],
])

testing_menu_kid_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ingliz tili testi", callback_data='english_test_kid_uzb')
    ],
    [
        InlineKeyboardButton(text='IQ testi', callback_data='iq_test_kid_uzb')
    ],
    [
        InlineKeyboardButton(text='Mantiqiy fikrlash testi', callback_data='logic_test_kid_uzb')
    ],
    [
        InlineKeyboardButton(text="Изменить язык", callback_data='lang')
    ],
])

testing_menu_18_uzb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Ingliz tili testi', callback_data='english_test_uzb')
    ],
    [
        InlineKeyboardButton(text='IQ testi', callback_data='iq_test_uzb')
    ],
    [
        InlineKeyboardButton(text='Mantiqiy fikrlash testi', callback_data='logic_test_uzb')
    ],
    [
        InlineKeyboardButton(text="Изменить язык", callback_data='lang')
    ],
])
