# Здесь храним все перменные и методы для их чтения и установки (а-ля работа с классами)
import view
from random import randint
from aiogram import types

gameDict = dict()

def howMuchToTake(onTableConf):#вычисляем сколько конфет нужно взять пользователю
    if onTableConf < 29: return onTableConf
    else:
        if onTableConf%29 == 0: return randint(1,28)
        else: return onTableConf%29

async def addNewPlayer (message: types.Message): #Добавляем новую запись в словарь
    global gameDict
    if message.from_user.id in gameDict: #продолжение игры
        await view.gameAlreadyStarted(message) #сообщаем что игра ещё не закончена
    else: #Начинаем игру
        gameDict[message.from_user.id] = 150
    await view.showConfets(message)
    # print (gameDict)

async def userTake (message: types.Message, confCount): #Пользователь берет конфеты
    global gameDict
    if gameDict[message.from_user.id] < confCount: confCount = gameDict[message.from_user.id] #Проверка на случай если взял больше чем есть
    gameDict[message.from_user.id] -= confCount
    await view.showPlayerTake(message,confCount)
    await view.showConfets(message)
    await checkWiner(message, 1)
    await botTake(message)


async def botTake (message: types.Message):
    global gameDict
    if not message.from_user.id in gameDict: return #не делаем ход бота если нет записи в словаре
    confCount = howMuchToTake(gameDict[message.from_user.id])
    gameDict[message.from_user.id] -= confCount
    await view.showBotTake(message,confCount)
    await view.showConfets(message)
    await checkWiner(message, 0)

def endGame(UserID): #Конец игры если осталось 0 конфет или по команде финиш
    global gameDict
    gameDict.pop(UserID)

async def checkWiner (message: types.Message,player):
    global gameDict
    if gameDict[message.from_user.id] == 0:
        if player: await view.showPlayerWin(message)
        else: await view.showBotWin(message)
        endGame(message.from_user.id)