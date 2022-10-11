# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся
# в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

def rle_pack(txt):
    result = ""
    i = 0
    while i < len(txt):
        symb = txt[i]
        count = 0
        while i < len(txt) and symb == txt[i]:
           count += 1
           i += 1
        result += str(count) + txt[i-1]
    return result

def rle_unpack(txt):
    result = ""
    tmp = ""
    count = 0
    for i in txt:
        if i in "0123456789":
            tmp += i
        else:
            result += i * int(tmp)
            tmp = ""
    return result


file_read = input("Введите имя файла для чтения: ")
file_write = input("Введите имя файла для вывода данных: ")

with open(file_read,"r") as f:
    text1=f.readline()

#определяем какой у нас первый символ - цифра или буква
if text1[0] in "0123456789":
    text2 = rle_unpack(text1)
else:
    text2 = rle_pack(text1)

print ("Содержимое файла с входными данными:")
print (text1)
print ("Содержимое файла с выходными данными:")
print (text2)

with open(file_write,"w") as f:
     f.write(text2)