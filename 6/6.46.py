n = int(input())
max_cifra = 0
min_cifra = 9
poz_max_end = 0
poz_min_end = 0
temp = n
poz = 0
while temp > 0:
    poz += 1
    cifra = temp % 10
    if cifra > max_cifra:
        max_cifra = cifra
        poz_max_end = poz
    if cifra < min_cifra:
        min_cifra = cifra
        poz_min_end = poz
    temp //= 10
total_poz = poz
poz_max_start = total_poz - poz_max_end + 1
poz_min_start = total_poz - poz_min_end + 1
print(poz_max_end, poz_max_start)
print(poz_min_end, poz_min_start)