massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
max_abs = abs(massiv[0])
for element in massiv:
    if abs(element) > max_abs:
        max_abs = abs(element)
print(max_abs)