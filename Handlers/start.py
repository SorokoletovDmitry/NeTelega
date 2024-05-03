from aiogram import Router, F 
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, CallbackQuery
from keyboards.start import *


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    """Обработка команды старт"""
    from main import bot
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='delete', description='Отчислиться'),
    ])

    await msg.answer(text="Страница 1", reply_markup=kb_start_next)

@router.callback_query(F.data == 'next')
async def next_handler(callback_query: CallbackQuery):
    """метод возвращающий к предыдущему действию"""
    await callback_query.message.edit_text(
        'Страница 2', reply_markup=kb_start_back)

@router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    """Копка отправляющая пользователя на действие вперед"""
    await callback_query.message.delete()
    await callback_query.message.answer(
        text='Страница 1', 
        reply_markup=kb_start_next)