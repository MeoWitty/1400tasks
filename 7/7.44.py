n = int(input())
summa = 0
znak = 1
for i in range(n):
    a = int(input())
    summa += znak * a
    znak = -znak
print(summa)