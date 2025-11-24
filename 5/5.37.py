n = int(input())
summa = 0
znak = 1
for i in range(1, n + 1):
    summa += znak * (1 / i)
    znak = -znak
print(summa)