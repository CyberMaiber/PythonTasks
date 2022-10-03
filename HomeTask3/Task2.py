# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random,math
n = int(input("Введите количество элементов в списке: "))
list = []
for i in range(0,n):
    list.append(random.randint(-n, n))
print ('Исходный список:')
print (list)

result_list = []

for i in range (0,math.ceil((len(list)/2))):
    result_list.append(list[i]*list[(len(list)-1)-i])

print ('Результат:')
print(result_list)