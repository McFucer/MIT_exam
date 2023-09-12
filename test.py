import asyncio
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils import executor

from app import on_startup

TOKEN = '6081189075:AAFSbM13QeKN9cowUPCMzBuNuhlGpSBT3Co'

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def timer_callback(message: types.Message, state: FSMContext):
    interval = 600  # Интервал времени в секундах (10 минут = 10 * 60 секунд)
    current_time = datetime.now()
    start_time = current_time

    while True:
        await asyncio.sleep(interval)  # Ожидаем 10 минут

        current_time = datetime.now()
        passed_time = current_time - start_time

        remaining_time = interval - passed_time.seconds

        if remaining_time <= 0:
            # Время вышло, отправляем табличку с данными и показываем всплывающее уведомление
            table = f"Прошло времени: {passed_time}"
            await message.answer(table, parse_mode=types.ParseMode.MARKDOWN)
            await bot.answer_callback_query(message.id, "Прошло 10 минут!", show_alert=True)

            # Переводим пользователя в состояние 'overall'
            await state.update_data(start_time=None)
            await state.finish()
            return

        await message.answer(f"Прошло {passed_time} минут.")

@dp.message_handler(Command('start_timer'))
async def start_timer(message: types.Message, state: FSMContext):
    await message.answer("Таймер запущен на 30 минут. Ожидайте...")


    # Создание и запуск таймера в отдельной задаче asyncio
    await asyncio.create_task(timer_callback(message, state))


@dp.message_handler(state='*')
async def handle_unknown_messages(message: types.Message):
    await message.answer("Неизвестная команда. Для запуска таймера введите /start_timer.")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)





