# a)
massiv = []
chislo = 300
count = 0
while count < 20:
    if chislo % 13 == 0 and chislo % 17 == 0:
        massiv.append(chislo)
        count += 1
    chislo += 1
for element in massiv:
    print(element)

# б)
massiv = []
chislo = 2
count = 0
while count < 30:
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