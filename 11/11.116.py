massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
index_max = 0
index_min = 0
for i in range(1, len(massiv)):
    if massiv[i] > massiv[index_max]:
        index_max = i
    if massiv[i] < massiv[index_min]:
        index_min = i
print(f"Index max: {index_max}, Index min: {index_min}")