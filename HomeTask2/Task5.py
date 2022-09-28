# 5. Реализуйте алгоритм перемешивания списка.
import random

list = []

#Заполнение списка который будем перемешивать
for i in range(0,20):
    list.append(i + 1)
print ("Заданный список:")
print (list)
mixed_list = []
for i in range(0,20):
    pos = random.randint(0, len(list) - 1)
    mixed_list.append(list[pos])
    list.remove(list[pos])
print("Перемешанный список:")
print(mixed_list)