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
    await asyncio.sleep(1800)  # Таймер на 30 минут (30 * 60 секунд)

    await state.finish()  # Завершение текущего состояния
    await state.set_state('another_state')  # Установка нового состояния

    await message.answer("Таймер завершен. Вы попали в другое состояние.")


@dp.message_handler(Command('start_timer'))
async def start_timer(message: types.Message, state: FSMContext):
    await message.answer("Таймер запущен на 30 минут. Ожидайте...")

    await state.set_state('timer')  # Установка состояния

    # Создание и запуск таймера в отдельной задаче asyncio
    await asyncio.create_task(timer_callback(message, state))


@dp.message_handler(state='*')
async def handle_unknown_messages(message: types.Message):
    await message.answer("Неизвестная команда. Для запуска таймера введите /start_timer.")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)





