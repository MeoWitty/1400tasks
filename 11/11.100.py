massiv = [5, 4, 3, 2, 5, 4, 3, 2, 5, 4, 3, 2, 5, 4, 3, 2, 5, 4, 3, 2, 5, 4]
srednyaya = sum(massiv) / len(massiv)
count = 0
for i in range(len(massiv)):
    if massiv[i] < srednyaya:
        count += 1
        print(i)
print("Vsego takikh uchenikov:", count)