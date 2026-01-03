massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
summa = sum(massiv)
count = 0
for i in range(len(massiv)):
    if massiv[i] > summa:
        count += 1
        print(i)
print("Vsego takikh:", count)