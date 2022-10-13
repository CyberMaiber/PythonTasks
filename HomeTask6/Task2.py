# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст: ")
lst = text.split(" ")

# result = []
# for word in lst:
#     if not "абв" in word:
#         result.append(word)
# выполняем используя filter()
result = list(filter(lambda x: not "абв" in x, lst))

print("Результат:")
print(" ".join(result))