# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Введите количество элементов в списке Фибоначчи: '))

lst = [0,1]

for i in range(1,k):
    lst.append(lst[i]+lst[i-1])

# temp_lst = []
# for i in range(1,k+1):
#     temp_lst.insert(0, (-1)**(i+1)*lst[i])
temp_lst = list(map(lambda x:(-1)**(x[0]+1)*x[1],enumerate(lst)))
#короче не получилось, зато понятно стало что такое enumerate :)
temp_lst.reverse()
lst.remove(0)
print(temp_lst+lst)
