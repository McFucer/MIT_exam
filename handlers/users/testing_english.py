from aiogram.types import CallbackQuery


from keyboards.inline.others import exam_kidoreld, exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, \
    testing_menu_18_uzb, testing_menu_kid, iq_test_kid
from keyboards.inline.inline_KBs import lang, quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, \
    quest10, quest11, quest12, quest13, quest14, quest15, quest16, quest17, quest18, quest19, quest20, quest21, quest22, \
    quest23, quest24, quest25, quest26, quest27, quest28, quest29, quest30, quest31, quest32, quest33, quest34, quest35, \
    quest36, quest37, quest38, quest39, quest40, quest41, quest42, quest43, quest44, quest45, quest46, quest47, quest48, \
    quest49, quest50, quest51, quest52, quest53, quest54, quest55, quest56, quest57, quest58, quest59, quest60

from loader import dp, db, bot
from keyboards.inline.others import iq_test

import sqlite3
import asyncio
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.others import exam_kidoreld,exam_kidoreld_uzb, testing_menu_kid_uzb, testing_menu_18, testing_menu_18_uzb, testing_menu_kid
from keyboards.inline.inline_KBs import lang, quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, \
    quest10, quest11, quest12, quest13, quest14, quest15, quest16, quest17, quest18, quest19, quest20, quest21, quest22, \
    quest23, quest24, quest25, quest26, quest27, quest28, quest29, quest30, quest31, quest32, quest33, quest34, quest35, \
    quest36, quest37, quest38, quest39, quest40

from loader import dp, db, bot




@dp.callback_query_handler(text='english_test_kid',state=['Russian','Uzbek'])
async def EnglishTest_kid(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await state.set_state('english_test')
    await call.message.answer('''1/60
I ______ bus on Mondays.
a.'m going to work with
b.'m going to work by
c.go to work with
d.go to work by''',reply_markup = quest1)

@dp.callback_query_handler(lambda c: c.data,state="english_test")
async def testing_started(call:CallbackQuery):
    await call.message.delete()
    q2 = '''2/60
Sorry, but this chair is ______.
a.me
b.mine
c.my
d.our'''
    q3 = '''3/60
A: 'How old ______?'   B: 'I ______ .'
a.are you / am 20 years old.
b.have you / have 20 years old
c.are you / am 20 years.
d.do you have / have 20 years.'''
    q4 = '''4/60
I ______ to the cinema.
a.not usually go
b.don't usually go
c.don't go usually
d.do not go usually'''
    q5 = '''5/60
Where ______ ?
a.your sister works
b.your sister work
c.does your sister work
d.do your sister work'''
    q6 = '''6/60
The test is ______ February.
a.in
b.at
c.on
d.over'''
    q7 = '''7/60
I eat pasta ______ week.
a.twice in a
b.twice a
c.one time a
d.once in a'''
    q8 = '''8/60
I don't have ______ free time.
a.many
b.any
c.a lot
d.some'''
    q9 = '''9/60
A: '_____ to the cinema tomorrow?'
a.We will go
b.Do we go
c.We go
d.Shall we go'''
    q10 = '''10/60
We went to the market ______ some vegetables.
a.to buy
b.for buy
c.for to buy
d.for buying'''
    q11 = '''11/60
Sorry, but when you called I ______ a shower.
a.had
b.did have
c.was having
d.were having'''
    q12 = '''12/60
______ are very friendly and very intelligent.
a.Dolphins
b.The dolphins
c.A dolphin
d.The dolphin'''
    q13 = '''13/60
Somebody stole ______ yesterday.
a.the car of my mother
b.my car mother
c.my mother's car
d.my mother car'''
    q14 = '''14/60
______ with me?
a.Do you like to dance
b.Would you like to dance
c.Do you like dance
d.Would you like dancing'''
    q15 = '''15/60
She is ______ her sister, I think.
a.more happier than
b.more happy that
c.happier that
d.happier than'''
    q16 = '''16/60
I couldn't eat ______ before the exam.
a.nothing
b.anything
c.everything
d.something'''
    q17 = '''17/60
Please, pass me the remote. ______ TV.
a.I'm watching
b.I will watch
c.I'm going to watch
d.I might watch'''
    q18 = '''18/60
I'll call you when I ______ home.
a.arrive
b.'m going to arrive
c.will arrive
d.arrived'''
    q19 = '''19/60
______ Japan?
a.Have you ever gone in
b.Do you have been in
c.Have you ever been to
d.Have you ever been into'''
    q20 = '''20/60
He drives very ______.
a.slow
b.slower
c.more slowly
d.slowly'''
    q21 = '''21/60
Can you ______ the lights? I can't see.
a.open
b.turn on
c.start
d.put on'''
    q22 = '''22/60
We couldn't find a taxi, ______ we walked home.
a.so
b.because
c.but
d.although'''
    q23 = '''23/60
Tomorrow I ______ get up early; it's my day off.
a.mustn't
b.must
c.haven't to
d.don't have to'''
    q24 = '''24/60
I ______ this coffee. It tastes horrible.
a.am not like
b.don't like
c.'m not liking
d.not like'''
    q25 = '''25/60
We ______ yesterday.
a.arrived
b.did arrive
c.have arrive
d.have arrived'''
    q26 = '''26/60
When I arrive home, I'm going to have a ______ bath.
a.relaxing
b.relaxed
c.relax
d.relaxation'''
    q27 = '''27/60
A: 'We don't have any milk.'   B: 'Really? I ______ more.'
a.'m going to buy
b.'ll buy
c.'m buying
d.buy'''
    q28 = '''28/60
We ______ to seeing you next Thursday.
a.really want
b.hope
c.are looking forward
d.really wish'''
    q29 ='''29/60
I'd like to go ______ in the park.
a.to walking
b.for walk
c.for a walk
d.to walk'''
    q30 = '''30/60
German ______ in Germany, Austria and Switzerland.
a.is spoken
b.spoken
c.speaks
d.is speak'''
    q31 = '''31/60
I ______ your book. It's fantastic. I'll finish it tonight.
a.'ve been reading
b.read
c.'ve read
d.'m read'''
    q32 = '''32/60
He went on a business _____ to New York.
a.travel
b.journey
c.commute
d.trip'''
    q33 = '''33/60
If I tell you a secret, ______ anyone?
a.are you tell
b.do you tell
c.will you tell
d.are you telling'''
    q34 = '''34/60
My brother and I don't ______ very well.
a.get off
b.get on
c.go on
d.break off'''
    q35 = '''35/60
I ______ fifty pages, but I have to read fifty more.
a.'ve been reading
b.was reading
c.'ve reading
d.'ve read'''
    q36 = '''36/60
If I ______ you, I wouldn't do it.
a.was
b.were
c.would be
d.am'''
    q37 = '''37/60
This painting ______ a fortune.
a.is worth
b.is value
c.values
d.worths'''
    q38 = '''38/60
She is the same age ______ me.
a.than
b.that
c.what
d.as'''
    q39 = '''39/60
It's obvious that you...
a.don't drive as faster as me.
b.drive faster than me.
c.drive more fast than I.
d.drive no faster than I.'''
    q40 = '''40/60
The boat sank, but they ______ swim to the shore.
a.could
b.were able to
c.can
d.abled to'''

    id = call.from_user.id
    if call.data == 'd1':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)

        await call.message.answer(q2 , reply_markup=quest2)
    elif call.data in ["a1", "b1", "c1"]:
        await call.message.answer(q2, reply_markup=quest2)


    elif call.data == 'b2':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q3 , reply_markup=quest3)
    elif call.data in ["a2", 'd2', 'c2']:
        await call.message.answer(q3 , reply_markup=quest3)

    elif call.data == 'a3':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q4 , reply_markup=quest4)
    elif call.data in ["d3" , 'b3' , 'c3']:
        await call.message.answer(q4 , reply_markup=quest4)

    elif call.data == 'b4':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q5 , reply_markup=quest5)
    elif call.data in ["a4" , 'd4' , 'c4']:
        await call.message.answer(q5 , reply_markup=quest5)
    if call.data == 'c5':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q6 , reply_markup=quest6)
    elif call.data == "a5" or call.data =='b5' or call.data == 'd5':
        await call.message.answer(q6 , reply_markup=quest6)

    if call.data == 'a6':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q7 , reply_markup=quest7)
    elif call.data == "d6" or call.data =='b6' or call.data =='c6':
        await call.message.answer(q7 , reply_markup=quest7)

    if call.data == 'b7':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q8 , reply_markup=quest8)
    elif call.data == "a7" or call.data =='d7' or call.data =='c7':
        await call.message.answer(q8 , reply_markup=quest8)

    if call.data == 'b8':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q9 , reply_markup=quest9)
    elif call.data == "a8" or call.data =='d8' or call.data =='c8':
        await call.message.answer(q9 , reply_markup=quest9)

    if call.data == 'd9':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q10 , reply_markup=quest10)
    elif call.data == "a9" or call.data =='b9' or call.data =='c9':
        await call.message.answer(q10 , reply_markup=quest10)

    if call.data == 'a10':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q11 , reply_markup=quest11)
    elif call.data == "b10" or call.data =='d10' or call.data =='c10':
        await call.message.answer(q11 , reply_markup=quest11)

    if call.data == 'c11':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q12 , reply_markup=quest12)
    elif call.data == "b11" or call.data =='d11' or call.data =='a11':
        await call.message.answer(q12 , reply_markup=quest12)

    if call.data == 'a12':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q13 , reply_markup=quest13)
    elif call.data == "b12" or call.data =='d12' or call.data =='c12':
        await call.message.answer(q13 , reply_markup=quest13)

    if call.data == 'c13':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q14 , reply_markup=quest14)
    elif call.data == "b13" or call.data =='d13' or call.data =='a13':
        await call.message.answer(q14 , reply_markup=quest14)

    if call.data == 'b14':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q15 , reply_markup=quest15)
    elif call.data == "c14" or call.data =='d14' or call.data =='a14':
        await call.message.answer(q15 , reply_markup=quest15)

    if call.data == 'd15':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q16 , reply_markup=quest16)
    elif call.data == "c15" or call.data =='b15' or call.data =='a15':
        await call.message.answer(q16 , reply_markup=quest16)

    if call.data == 'b16':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q17 , reply_markup=quest17)
    elif call.data == "c16" or call.data =='d16' or call.data =='a16':
        await call.message.answer(q17 , reply_markup=quest17)

    if call.data == 'c17':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q18 , reply_markup=quest18)
    elif call.data == "b17" or call.data =='d17' or call.data =='a17':
        await call.message.answer(q18 , reply_markup=quest18)

    if call.data == 'a18':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q19 , reply_markup=quest19)
    elif call.data == "b18" or call.data =='d18' or call.data =='c18':
        await call.message.answer(q19 , reply_markup=quest19)

    if call.data == 'c19':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q20 , reply_markup=quest20)
    elif call.data == "b19" or call.data =='d19' or call.data =='a19':
        await call.message.answer(q20 , reply_markup=quest20)

    if call.data == 'd20':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q21 , reply_markup=quest21)
    elif call.data == "c20" or call.data =='b20' or call.data =='a20':
        await call.message.answer(q21 , reply_markup=quest21)

    if call.data == 'b21':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q22 , reply_markup=quest22)
    elif call.data == "c21" or call.data =='d21' or call.data =='a21':
        await call.message.answer(q22 , reply_markup=quest22)

    if call.data == 'a22':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q23 , reply_markup=quest23)
    elif call.data == "c22" or call.data =='d22' or call.data =='b22':
        await call.message.answer(q23 , reply_markup=quest23)

    if call.data == 'd23':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q24 , reply_markup=quest24)
    elif call.data == "c23" or call.data =='a23' or call.data =='b23':
        await call.message.answer(q24 , reply_markup=quest24)

    if call.data == 'b24':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q25 , reply_markup=quest25)
    elif call.data == "c24" or call.data =='a24' or call.data =='d24':
        await call.message.answer(q25 , reply_markup=quest25)

    if call.data == 'a25':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q26 , reply_markup=quest26)
    elif call.data == "c25" or call.data =='b25' or call.data =='d25':
        await call.message.answer(q26 , reply_markup=quest26)

    if call.data == 'a26':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q27 , reply_markup=quest27)
    elif call.data == "c26" or call.data =='b26' or call.data =='d26':
        await call.message.answer(q27 , reply_markup=quest27)

    if call.data == 'b27':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q28 , reply_markup=quest28)
    elif call.data == "c27" or call.data =='a27' or call.data =='d27':
        await call.message.answer(q28 , reply_markup=quest28)

    if call.data == 'c28':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q29 , reply_markup=quest29)
    elif call.data == "b28" or call.data =='a28' or call.data =='d28':
        await call.message.answer(q29 , reply_markup=quest29)

    if call.data == 'c29':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q30 , reply_markup=quest30)
    elif call.data == "b29" or call.data =='a29' or call.data =='d29':
        await call.message.answer(q30 , reply_markup=quest30)

    if call.data == 'a30':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q31 , reply_markup=quest31)
    elif call.data == "b30" or call.data =='c30' or call.data =='d30':
        await call.message.answer(q31 , reply_markup=quest31)

    if call.data == 'a31':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q32 , reply_markup=quest32)
    elif call.data == "b31" or call.data =='c31' or call.data =='d31':
        await call.message.answer(q32 , reply_markup=quest32)

    if call.data == 'd32':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q33 , reply_markup=quest33)
    elif call.data == "b32" or call.data =='c32' or call.data =='a32':
        await call.message.answer(q33 , reply_markup=quest33)

    if call.data == 'c33':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q34 , reply_markup=quest34)
    elif call.data == "b33" or call.data =='d33' or call.data =='a33':
        await call.message.answer(q34 , reply_markup=quest34)

    if call.data == 'b34':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q35 , reply_markup=quest35)
    elif call.data == "c34" or call.data =='d34' or call.data =='a34':
        await call.message.answer(q35 , reply_markup=quest35)

    if call.data == 'd35':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q36 , reply_markup=quest36)
    elif call.data == "c35" or call.data =='b35' or call.data =='a35':
        await call.message.answer(q36 , reply_markup=quest36)

    if call.data == 'b36':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q37 , reply_markup=quest37)
    elif call.data == "c36" or call.data =='d36' or call.data =='a36':
        await call.message.answer(q37 , reply_markup=quest37)

    if call.data == 'a37':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q38 , reply_markup=quest38)
    elif call.data == "c37" or call.data =='d37' or call.data =='b37':
        await call.message.answer(q38 , reply_markup=quest38)

    if call.data == 'd38':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q39 , reply_markup=quest39)
    elif call.data == "c38" or call.data =='a38' or call.data =='b38':
        await call.message.answer(q39 , reply_markup=quest39)

    if call.data == 'b39':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer(q40 , reply_markup=quest40)
    elif call.data == "c39" or call.data =='a39' or call.data =='d39':
        await call.message.answer(q40 , reply_markup=quest40)

    if call.data == 'b40':
        try:
            user = db.select_user_s(id=id)
            if user:
                current_result = user['result_english']
                new_result = current_result + 1
                db.edit_english_result(result=new_result, id=id)
                print(f"User's result_english incremented to: {new_result}")
            else:
                print("User not found.")
        except Exception as err:
            print(err)
        await call.message.answer("Перейти к след. тесту | Keyingi testga o'tish",reply_markup=iq_test_kid)
    elif call.data == "c40" or call.data =='a40' or call.data =='d40':
        await call.message.answer("Перейти к след. тесту | Keyingi testga o'tish",reply_markup=iq_test_kid)

