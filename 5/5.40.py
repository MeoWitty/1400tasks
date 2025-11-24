chislo = int(input())
summa = 0
while chislo > 0:
    summa += chislo % 10
    chislo //= 10
print(summa)