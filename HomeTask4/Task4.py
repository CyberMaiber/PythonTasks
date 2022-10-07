# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
import random
lst = []
text = ""
k = int(input("Введите k: "))
for i in range(0,k+1):
    lst.append(random.randint(0, 100))
# print (lst)
for i in reversed(range(0,k+1)):
    if i != 0: 
        if lst[i] != 0:
            text += f"{lst[i]}*X^{i} + "
    else:
        text += f"{lst[i]} = 0"
with open ("f_task4.txt","w") as f:
    f.write(text)
print ("Файл записан.")