summa = 0
klass = 1
while klass <= 11:
    deti = int(input())
    if klass % 2 != 0:
        summa += deti
    klass += 1
print(summa)