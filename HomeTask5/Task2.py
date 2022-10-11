# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random
conf_count = 150
current_player = (random.randint(1,1000)%2) == 0 #бросаем жребий какой игрок первым ходит (игрок или компьютер)
while conf_count != 0: #тело программы
    print(f"Количество конфет на столе: {conf_count}")
    if current_player:
        print("Ход человека.", end = " ")
        player_take = 0
        while player_take < 1 or player_take > 28:
            player_take = int(input("Сколько конфет вы хотите взять? "))
            if player_take < 1 or player_take > 28:
                print("Количество конфет должно быть в пределах от 1 до 28.")
    else:
        print("Ход ИИ.", end = " ")
        player_take = (conf_count%29)
        if player_take > 28: player_take = 28
        if conf_count < 29: player_take = conf_count
        if player_take == 0: player_take = 1
        print(f"ИИ взял конфет: {player_take}")
    conf_count -= player_take
    if not conf_count:
        print(f"Количество конфет на столе: {conf_count}")
        if current_player:
            print("Победил человек.")
        else:
            print("Победил ИИ.")
        break
    else:
        current_player = not current_player #переход хода