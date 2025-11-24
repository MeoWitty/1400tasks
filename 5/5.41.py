chislo = int(input())
n = int(input())
proizv = 1
summa = 0
for i in range(n):
    cifra = chislo % 10
    proizv *= cifra
    summa += cifra
    chislo //= 10
print(proizv)
print(summa)