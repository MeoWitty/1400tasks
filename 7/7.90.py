est_troika = False
for i in range(12):
    ocenka = int(input())
    if ocenka == 3:
        est_troika = True
if not est_troika:
    print("Да")
else:
    print("Нет")