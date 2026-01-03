massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
srednee = sum(massiv) / len(massiv)
minimum = min(massiv)
maximum = max(massiv)
porog = (minimum + maximum) / 2
count = 0
for i in range(len(massiv)):
    if massiv[i] > porog:
        count += 1
        print(i)
print("Vsego takikh:", count)