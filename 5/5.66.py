summa = 0
for n in range(1, 13):
    kvad = 0
    for i in range(1, 2 * n, 2):
        kvad += i
    summa += kvad
print(summa)