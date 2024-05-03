'''Импорт модулей и кода из соседних файлов в папке'''
from aiogram import Dispatcher

from handlers import anketa, start

def include_routers(dp: Dispatcher):
    dp.include_routers(

    start.router,
    anketa.router
    )
    