nomer_666 = 0
i = 1
while True:
    chislo = int(input())
    if chislo == 100:
        break
    if chislo == 666 and nomer_666 == 0:
        nomer_666 = i
    i += 1
print(nomer_666)