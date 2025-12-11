summa = 0
znak = -1
for i in range(15):
    c = float(input())
    summa += znak * c
    znak = -znak
print(summa)