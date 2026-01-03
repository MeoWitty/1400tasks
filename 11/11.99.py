massiv = [5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6, 0, 9, 0, 1, 0, 5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6]
srednee = sum(massiv) / len(massiv)
count = 0
for i in range(len(massiv)):
    if massiv[i] > srednee:
        count += 1
        print(i+1)  # номер дня
print("Vsego takikh dney:", count)