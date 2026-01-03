massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
index_max_abs = 0
for i in range(1, len(massiv)):
    if abs(massiv[i]) > abs(massiv[index_max_abs]):
        index_max_abs = i
print(index_max_abs)