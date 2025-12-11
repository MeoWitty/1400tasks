dney_bez_osadkov = 0
for den in range(1, 32):
    osadki = float(input())
    if osadki == 0:
        dney_bez_osadkov += 1
if dney_bez_osadkov >= 10:
    print("Да")
else:
    print("Нет")