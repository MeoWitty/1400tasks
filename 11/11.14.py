chislo = int(input())
massiv = [0, 0, 0, 0, 0, 0]
index = 0
while chislo > 0:
    massiv[index] = chislo % 10
    chislo = chislo // 10
    index += 1
for cifra in massiv:
    if cifra != 0:
        print(cifra)