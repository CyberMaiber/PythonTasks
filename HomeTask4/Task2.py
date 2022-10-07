n = int(input("n="))
lst = []
#Ищем простые числа от 2 до n
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
#Теперь ищем простые множители числа n
lst_of_muls = []
for i in lst:
    if n % i == 0:
        lst_of_muls.append(i)
        
print (lst_of_muls)

