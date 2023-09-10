import asyncio
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor

from app import on_startup

TOKEN = '6081189075:AAFSbM13QeKN9cowUPCMzBuNuhlGpSBT3Co'

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def timer_callback(message: types.Message, state: FSMContext):
    interval = 600  # Интервал времени в секундах (10 минут = 10 * 60 секунд)

    # Запускаем бесконечный цикл, который будет выполняться каждые 10 минут
    while True:
        await asyncio.sleep(interval)  # Ожидаем 10 минут

        # Получаем текущее время и сколько времени прошло с начала запуска таймера
        current_time = datetime.now()
        passed_time = current_time - message.date

        # Вычисляем оставшееся время в минутах
        remaining_time = interval // 60 - passed_time.seconds // 60

        # Отправляем сообщение с оповещением о прошедших 10 минутах и оставшемся времени
        await message.answer(f"Прошло 10 минут.")

    await state.set_state('overall')  # Перевод пользователя в состояние 'overall'


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





