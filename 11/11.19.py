massiv = []
chislo = 100
count = 0
while count < 10:
    prostoe = True
    for delitel in range(2, chislo):
        if chislo % delitel == 0:
            prostoe = False
            break
    if prostoe:
        massiv.append(chislo)
        count += 1
    chislo += 1
for element in massiv:
    print(element)