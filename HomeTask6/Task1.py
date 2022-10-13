# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов. Mинимальное значение дробной части отличное от нуля,
# у целых чисел дробной части нет их в расчет не берем
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

def dec_count(inp_num): #Подсчёт количества знаков после точки
    if math.trunc(inp_num) != inp_num:
        count = 0
        text = str(inp_num)
        for i in reversed(text):
            if i == ".":
                break
            else:
                count += 1
        return count
    else:
        return 0

list = [1.1, 1.2, 3.1, 5, 10.01]

cut = lambda flt:flt - math.trunc(flt) #Запиливаем лямбду

index_max_float = 1
index_min_float = 1
max_dec_count = 0

for i in range(0, len(list)):
    if math.trunc(list[i]) != list[i]:
        # if (list[i] - math.trunc(list[i]))>(list[index_max_float] - math.trunc(list[index_max_float])):index_max_float = i
        # if (list[i] - math.trunc(list[i]))<(list[index_min_float] - math.trunc(list[index_min_float])):index_min_float = i
        if cut(list[i])>cut(list[index_max_float]):index_max_float = i
        if cut(list[i])<cut(list[index_min_float]):index_min_float = i
        
        if dec_count(list[i]) > max_dec_count:max_dec_count = dec_count(list[i])
# print (round((list[index_max_float] - math.trunc(list[index_max_float]))-(list[index_min_float] - math.trunc(list[index_min_float])),max_dec_count))
print (round(cut(list[index_max_float])-cut(list[index_min_float]),max_dec_count))