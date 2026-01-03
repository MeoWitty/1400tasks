massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
index_max = 0
index_min = 0
for i in range(1, len(massiv)):
    if massiv[i] > massiv[index_max]:
        index_max = i
    if massiv[i] < massiv[index_min]:
        index_min = i
print(f"Nomer maksimuma: {index_max}")
print(f"Nomer minimuma: {index_min}")