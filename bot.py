import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token='6315324783:AAGVx4TmWdY9IcPe5-3BaFm2RUbYgTwhrI8')
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello!')

# Запуск процеса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())