massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
count = 0
for i in range(1, len(massiv)-1):
    if massiv[i] > massiv[i-1] and massiv[i] > massiv[i+1]:
        count += 1
print(count)