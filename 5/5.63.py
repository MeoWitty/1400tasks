summa = 0
znak = 1
for i in range(1, 19):
    summa += znak * (i ** 2)
    znak = -znak
print(summa)