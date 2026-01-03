massiv = [5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6, 0, 9, 0, 1, 0, 5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6]
summa = 0
count = 0
for element in massiv:
    if element > 0:
        summa += element
        count += 1
if count > 0:
    print(summa / count)
else:
    print("Net dozhdlinykh dney")