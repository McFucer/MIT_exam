from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = ['a', 'b', 'c', 'd']
markup = []

for i in range(1, 61):
    text = f'question{i}'
    callback_data = f'{texts[(i-1) % len(texts)]}{(i-1) // len(texts) + 1}'
    button = InlineKeyboardButton(text=text, callback_data=callback_data)
    markup.append([button])

keyboard = InlineKeyboardMarkup(inline_keyboard=markup)

# Вывод inline-клавиатуры с 60 текстами
print(keyboard.inline_keyboard)