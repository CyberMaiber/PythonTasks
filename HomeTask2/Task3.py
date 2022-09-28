# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


n = int(input("Введите натуральное число: "))
list = []
sum = 0

for i in range(1,n+1):
    list.append((1+1/i)**i)

for i in range(n):
    sum += list[i]
print ('Полученный список:')
print (list)

print (f"Сумма элементов списка: {sum}")