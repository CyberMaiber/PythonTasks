# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст: ")
list = text.split(" ")
result = []
for word in list:
    if not "абв" in word:
        result.append(word)

print("Результат:")
print(" ".join(result))