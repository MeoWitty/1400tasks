n = int(input())
max_cifra = 0
min_cifra = 9
poz_max_start = 0
poz_min_start = 0
temp = n
poz = 0
while temp > 0:
    poz += 1
    cifra = temp % 10
    if cifra > max_cifra:
        max_cifra = cifra
        poz_max_start = poz
    if cifra < min_cifra:
        min_cifra = cifra
        poz_min_start = poz
    temp //= 10
total_poz = poz
poz_max_start = total_poz - poz_max_start + 1
poz_min_start = total_poz - poz_min_start + 1
if poz_max_start < poz_min_start:
    print("Максимальная")
else:
    print("Минимальная")