summa = 0
znak = -1
for i in range(1, 11):
    summa += znak * (i ** 2)
    znak = -znak
print(summa)