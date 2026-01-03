massiv = [5, 25, 12, 30, 7, 18, 21, 15, 22, 6]
summa = 0
count = 0
for element in massiv:
    if element > 10:
        summa += element
        count += 1
if count > 0:
    print(summa / count)
else:
    print("Net takikh elementov")