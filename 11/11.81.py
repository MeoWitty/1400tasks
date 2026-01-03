massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
count = 0
for i in range(len(massiv)-1):
    if massiv[i] % 2 == 0 and massiv[i+1] % 2 == 0:
        count += 1
print(count)