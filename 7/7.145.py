n = int(input())
ocenki = []
for i in range(n):
    ocenka = float(input())
    ocenki.append(ocenka)

max_ocenka = max(ocenki)
min_ocenka = min(ocenki)

summa = 0
count = 0
max_udalena = False
min_udalena = False

for ocenka in ocenki:
    if ocenka == max_ocenka and not max_udalena:
        max_udalena = True
        continue
    if ocenka == min_ocenka and not min_udalena:
        min_udalena = True
        continue
    summa += ocenka
    count += 1

print(summa / count)