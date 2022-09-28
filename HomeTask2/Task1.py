# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

# Вариант с переводом в текст
def via_text (inp_num):
    sum = 0
    text = str(inp_num)
    for i in range(len(text)):
        if text[i] != "," and text[i] != ".":sum+=int(text[i])
    return sum
    
# Вариант без перевода в текст
def via_mul (inp_num):
    sum = 0
    while inp_num != int(inp_num):
        inp_num *= 10
    int_num = int(inp_num)
    
    while inp_num != 0:
        sum += inp_num%10
        inp_num = int(inp_num/10)
    return int(sum)


num = float(input("Введите вещественное число: "))

# print(f"Сумма цифр числа равна {via_text(num)}")

print(f"Сумма цифр числа равна {via_mul(num)}")

