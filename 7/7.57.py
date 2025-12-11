sum_chet = 0
sum_nechet = 0
for den in range(1, 31):
    osadki = float(input())
    if den % 2 == 0:
        sum_chet += osadki
    else:
        sum_nechet += osadki
if sum_chet > sum_nechet:
    print("Да")
else:
    print("Нет")