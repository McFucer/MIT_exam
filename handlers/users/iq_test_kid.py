import sqlite3
import asyncio
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.others import exam_kidoreld,exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, testing_menu_18_uzb, testing_menu_kid
from keyboards.inline.inline_KBs import lang,  markup_cont
from keyboards.inline.iq_test import quest1, quest2, quest3, quest4, quest5, quest10, quest6, quest7, quest8, quest9, \
    quest11, quest12, quest13, quest14, quest15, quest16, quest17, quest18, quest19, quest20, quest21, quest22, quest23, \
    quest24, quest25
from loader import dp, db, bot



@dp.callback_query_handler(text='iq_test_kid', state='*')
async def starting_iq(call:CallbackQuery, state: FSMContext):
    await state.set_state('exam_iq')
    path_to_photo = r"D:/Новая папка (2)/mukammal-bot-paid-db_sqlite/photo's/example.jpg"
    photo_file = types.InputFile(path_to_photo)
    await call.message.delete()
    await call.message.answer_photo(
        photo=photo_file,caption='Отвечайте на вопросы по такой порядке! Здесь 25 вопросов | Savollarga shu tartibda javob bering! Bu yerda 25 ta savol bor\n<b>IQ test: 25 savol |IQ test: 25 вопрсов</b>',reply_markup=markup_cont)

@dp.callback_query_handler(text='iqtest_started',state='exam_iq')
async def fir(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\1.jpg"),reply_markup=quest1)



@dp.callback_query_handler(lambda c: c.data,state="exam_iq")
async def iq_test(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    id = call.from_user.id
    if call.data == '1.2':
        await call.message.answer_photo(caption='1/25',
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\2.jpg"),
        reply_markup=quest2)
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\2.jpg"),
            reply_markup=quest2)

    if call.data == '2.6':
        await call.message.answer_photo(caption='2/25',
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\3.jpg"),
        reply_markup=quest3)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['2.1','2.2','2.3','2.4','2.5','2.7','2.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\3.jpg"),
            reply_markup=quest3)

    if call.data == '3.2':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\4.jpg"),
        reply_markup=quest4)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\4.jpg"),
            reply_markup=quest4)

    if call.data == '4.3':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\5.jpg"),
        reply_markup=quest5)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['4.1','4.2','4.4','4.5','4.6','4.7','4.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\5.jpg"),
            reply_markup=quest5)

    if call.data == '5.1':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\6.jpg.jpg"),
        reply_markup=quest6)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['5.2','5.3','5.4','5.5','5.6','5.7','5.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\6.jpg"),
            reply_markup=quest6)

    if call.data == '6.5':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\7.jpg"),
        reply_markup=quest7)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['6.1','6.2','6.3','6.4','6.6','6.7','6.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\7.jpg"),
            reply_markup=quest7)

    if call.data == '7.2':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\8.jpg"),
        reply_markup=quest8)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\8.jpg"),
            reply_markup=quest8)

    if call.data == '8.1':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\9.jpg"),
        reply_markup=quest9)
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['8.2','8.3','8.4','8.5','8.6','8.7','8.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\9.jpg"),
            reply_markup=quest9)

    if call.data == '9.3':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\10.jpg"),
        reply_markup=quest10)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['9.1','9.2','9.4','9.5','9.6','9.7','9.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\10.jpg"),
            reply_markup=quest10)

    if call.data == '10.6':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\11.jpg"),
        reply_markup=quest11)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['10.1','10.2','10.3','10.4','10.5','10.7','10.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\11.jpg"),
            reply_markup=quest11)

    if call.data == '11.3':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\12.jpg"),
        reply_markup=quest12)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['11.1','11.2','11.4','11.5','11.6','11.7','11.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\12.jpg"),
            reply_markup=quest12)

    if call.data == '12.5':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\13.jpg"),
        reply_markup=quest13)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['12.1','12.2','12.3','12.4','12.6','12.7','12.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\13.jpg"),
            reply_markup=quest13)

    if call.data == '13.2':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\14.jpg"),
        reply_markup=quest14)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['13.1','13.2','13.3','13.4','13.5','13.6','13.7','13.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\14.jpg"),
            reply_markup=quest14)

    if call.data == '14.7':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\15.jpg"),
        reply_markup=quest15)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['14.1','14.2','14.3','14.4','14.5','14.6','14.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\15.jpg"),
            reply_markup=quest15)

    if call.data == '15.1':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\16.jpg"),
        reply_markup=quest16)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['15.2','15.3','15.4','15.5','15.6','15.7','15.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\16.jpg"),
            reply_markup=quest16)

    if call.data == '16.2':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\17.jpg"),
        reply_markup=quest17)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['16.1','16.2','16.3','16.4','16.5','16.6','16.7','16.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\17.jpg"),
            reply_markup=quest17)

    if call.data == '17.2':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\18.jpg"),
        reply_markup=quest18)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['17.1','17.2','17.3','17.4','17.5','17.6','17.7','17.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\18.jpg"),
            reply_markup=quest18)

    if call.data == '18.5':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\19.jpg"),
        reply_markup=quest19)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['18.1','18.2','18.3','18.4','18.5','18.6','18.7','18.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\19.jpg"),
            reply_markup=quest19)

    if call.data == '19.4':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\20.jpg"),
        reply_markup=quest20)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['19.1','19.2','19.3','19.4','19.5','19.6','19.7','19.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\20.jpg"),
            reply_markup=quest20)

    if call.data == '20.1':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\21.jpg"),
        reply_markup=quest21)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['20.1','20.2','20.3','20.4','20.5','20.6','20.7','20.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\21.jpg"),
            reply_markup=quest21)

    if call.data == '21.4':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\22.jpg"),
        reply_markup=quest22)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['21.1','21.2','21.3','21.4','21.5','21.6','21.7','21.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\22.jpg"),
            reply_markup=quest22)

    if call.data == '22.8':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\23.jpg"),
        reply_markup=quest23)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['22.1','22.2','22.3','22.4','22.5','22.6','22.7','22.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\23.jpg"),
            reply_markup=quest23)

    if call.data == '23.7':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\24.jpg"),
        reply_markup=quest24)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['23.1','23.2','23.3','23.4','23.5','23.6','23.7','23.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\24.jpg"),
            reply_markup=quest24)

    if call.data == '24.6':
        await call.message.answer_photo(
        photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\25.jpg"),
        reply_markup=quest25)

        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
    elif call.data in ['24.1','24.2','24.3','24.4','24.5','24.6','24.7','24.8']:
        await call.message.answer_photo(
            photo=types.InputFile(r"D:\Новая папка (2)\mukammal-bot-paid-db_sqlite\photo's\25.jpg"),
            reply_markup=quest25)

    if call.data == '25.8':


        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_iq']
                new_result = current_result + 1
                db.edit_iq_result(result=new_result, id=id)
                print(f"User's result_iq incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)

        await call.message.answer('Test tugadi | Тест окончен')
        await state.set_state('Overall')

    elif call.data in ['25.1','25.2','25.3','25.4','25.5','25.6','25.7','25.8']:
        await call.message.answer('Test tugadi | Тест окончен')
        await state.set_state('Overall')



