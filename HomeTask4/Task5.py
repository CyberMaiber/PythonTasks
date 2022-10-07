# 5.	Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
def make_dict (txt):
    tdict = dict()
    while txt.find("^") != -1:
        place = txt.find("^")
        i = 1
        while txt[place + i] != "+" and txt[place + i] != "-":i += 1
        tdict[int(txt[place+1:place+i])]=int(txt[:place])
        txt = txt.replace(txt[:place] + "^" + txt[place+1:place+i],"")
    if len(txt) != 0:tdict[0] = int(txt)
    return tdict

def symint(integer):
    if integer>=0: return "+"+str(integer)
    else: return str(integer)

text1=""
text2=""

with open("f_task4.txt","r") as f:
    text1=f.readline()
with open("f_task4+.txt ","r") as f:
    text2=f.readline()
dict1 = dict()
dict2 = dict()
text1 = text1.replace("*X", "").replace(" = 0", "").replace(" ", "")
text2 = text2.replace("*X", "").replace(" = 0", "").replace(" ", "")
dict1 = make_dict (text1)
dict2 = make_dict (text2)
print (dict1)
print (dict2)
# объединяем словари
for key in dict2:
    if dict1.get(key) != None:dict1[key] += dict2[key]
    else: dict1[key] = dict2[key]
print (dict1)
#Ищем максимальный ключ в объединенном словаре
maxkey = 0
text1 = ""
for key in dict1:
    if key>maxkey:maxkey=key
#формируем строку для записи в файл
for i in reversed(range(0,maxkey+1)):
    if dict1.get(i) != None:
        if i != 0:
            if dict1[i] != 0:text1 += f"{symint(dict1[i])}*X^{i}"
        else:
            if dict1[i] != 0:text1 += f"{symint(dict1[i])}"
if text1[0] == "+":text1=text1[1:]
text1 += " = 0"
text1 = text1.replace("+", " + ").replace("-", " - ")
#Печатаем файл
with open ("f_task5.txt","w") as f:
    f.write(text1)
print ("Файл записан.")