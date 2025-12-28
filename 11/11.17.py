massiv = [1, 1]
for i in range(2, 10):
    massiv.append(massiv[i-1] + massiv[i-2])
for element in massiv:
    print(element)