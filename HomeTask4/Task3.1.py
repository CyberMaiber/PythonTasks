#Решение с помощью множеств
n = str(input("n="))
lst = list(n)
mng = set(lst)
alone = []
for i in mng:
    count = 0
    for j in range(len(lst)):
        if i == lst[j]:count += 1
    if count == 1:alone.append(i)
print (alone)
