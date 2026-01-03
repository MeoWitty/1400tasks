massiv = [5, 0, 0, 3, 7, 0, 0, 15, 2, 0]
count = 0
for i in range(len(massiv)-1):
    if massiv[i] == 0 and massiv[i+1] == 0:
        count += 1
print(count)