from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

gameDict = dict()

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('/hi - Приветствие\n/help - Справка\n/startplay - Начать играть\n/take - Взять конфеты (от 1 до 28)')
    

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')
    # await update.message.reply_text(f'ID {update.effective_user.id}')

async def startplay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id in gameDict: #проверям старый или новый игрок
        await update.message.reply_text(f'{update.effective_user.first_name}, продолжаем игру.')
    else:
        await update.message.reply_text(f'{update.effective_user.first_name}, начинаем игру с конфетами. Правила:на столе лежат конфеты,')
        await update.message.reply_text('игрок и бот по очереди берут конфеты - не более 28 штук за раз. Побеждает тот, кто заберёт последнюю конфету.')
        gameDict[update.effective_user.id] = 150
    await update.message.reply_text(f'На столе конфет: {gameDict[update.effective_user.id]}. Ваш ход.')

async def take(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_user.id in gameDict: #заставляем набрать startplay
        await update.message.reply_text('Для начала игры наберите /startplay')
        return
    try:
        playerTakeConf = int(update.message.text[6:])
        if playerTakeConf < 1 or playerTakeConf > 28:
            await update.message.reply_text('Число конфет должно быть от 1 до 28.')
            return
        else:
            gameDict[update.effective_user.id] -= playerTakeConf
    except:#исключение если не удалсь распознать число конфет, которые берет игрок
        await update.message.reply_text('Не удалось распознать количество забираемых конфет.')
        return
    if gameDict[update.effective_user.id] < 1: #Пользователь взял последние конфеты.
        await update.message.reply_text('Поздравляем! Вы выиграли!')
        gameDict.pop(update.effective_user.id)
        return
    else:
        #Ход ИИ
        playerTakeConf = howMuchToTake(gameDict[update.effective_user.id])
        gameDict[update.effective_user.id] -= playerTakeConf
        await update.message.reply_text(f'Бот забирает конфет: {playerTakeConf}.')
        if gameDict[update.effective_user.id] < 1:
            await update.message.reply_text('К сожалению, Вы проиграли. Бот забрал последнюю конфету.')
            gameDict.pop(update.effective_user.id)
            return
    await update.message.reply_text(f'На столе конфет: {gameDict[update.effective_user.id]}. Ваш ход.')

def howMuchToTake(onTableConf):
    if onTableConf < 29: return onTableConf
    else:
        if onTableConf%29 == 0: return 1
        else: return onTableConf%29

app = ApplicationBuilder().token("5657897259:AAHGRJuaF6qjchgoe2eAX5zXGi73wXz4ERE").build()

app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("startplay", startplay))
app.add_handler(CommandHandler("take", take))

app.run_polling()