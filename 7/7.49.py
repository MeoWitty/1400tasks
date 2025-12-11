summa = 0
for den in range(1, 31):
    osadki = float(input())
    if den % 2 == 0:
        summa += osadki
print(summa)