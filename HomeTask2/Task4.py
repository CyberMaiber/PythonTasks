# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

def r_line_fr_file (num):
    f = open('file.txt','r')
    for i in range(num):
        temp = f.readline()
    f.close()
    return int(temp)

import random

position1 = 3
position2 = 7
mul = 1
n = int(input("Введите натуральное число: "))
list = []
for i in range(0,n):
    list.append(random.randint(-n, n))
print ('Полученный список:')
print (list)
f = open('file.txt','w')
for i in range(0,n):
    print(list[i],file=f)
f.close()
print(f"Произведение чисел на позициях {position1} и {position2}:")
print(r_line_fr_file(position1) * r_line_fr_file(position2))

