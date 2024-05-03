"""Импорт модулей"""
import asyncio

from aiogram import Bot, Dispatcher
from handlers import imclude_routers

bot = Bot(token = '')
dp = Dispatcher()


async def main():
    """Запуск бота"""
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())