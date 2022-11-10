# юда все функции отправляющие сообщения


from aiogram import types

from bot import bot
import model

async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки')

async def gameNotStarted(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, игра ещё не начата!\n'
                           f'Наберите /start')

async def gameAlreadyStarted(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, игра уже начата!')

async def showConfets(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Конфет на столе: {model.gameDict[message.from_user.id]}')

async def showBotTake(message: types.Message, confCount):
    await bot.send_message(message.from_user.id,
                           f'Бот взял конфет: {confCount}')

async def showPlayerTake(message: types.Message, confCount):
    await bot.send_message(message.from_user.id,
                           f'Вы взяли конфет: {confCount}')

async def showPlayerWin(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, поздравляем! Вы выиграли!')

async def showBotWin(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, к сожалению, Вы проиграли. Бот забрал последнюю конфету.')

async def showWrongConfCount(message: types.Message):
    await bot.send_message(message.from_user.id, 'Число конфет должно быть от 1 до 28!')

async def showWrongInput(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите целое число от 1 до 28 - количество конфет, которое Вы хотите взять со стола.')