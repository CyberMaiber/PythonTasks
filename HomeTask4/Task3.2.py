#Решение с помощью какой-то другой магии
from collections import Counter
n = str(input("n="))
cnt = dict(Counter(n).most_common()[:-11:-1])
print (cnt)
lst = []
for k, v in cnt.items():
    if v == 1:lst.append(int(k))

print (lst)
