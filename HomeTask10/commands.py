# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view
import model
from bot import bot


async def start(message: types.Message):
    await view.greetings(message)
    await model.addNewPlayer(message)


async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')
    model.endGame(message.from_user.id)

async def getNumber(message: types.Message):
    playerTakeConf = message.text
    if not message.from_user.id in model.gameDict: #заставляем набрать start
        await view.gameNotStarted(message)
        return
    try:
        confCount = int(playerTakeConf)
        if confCount < 1 or confCount > 28:
            await view.showWrongConfCount
        else:
            await model.userTake(message,confCount)
    except:#исключение если не удалсь распознать число конфет, которые берет игрок
        await view.showWrongInput(message)
    