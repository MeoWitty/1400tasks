n = int(input())

# а
max_nechet = 0
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra % 2 != 0 and cifra > max_nechet:
        max_nechet = cifra
    temp //= 10
print(max_nechet)

# б
min_cifra = 9
poz_min = 0
temp = n
poz = 0
while temp > 0:
    poz += 1
    cifra = temp % 10
    if cifra < min_cifra:
        min_cifra = cifra
        poz_min = poz
    temp //= 10
total_poz = poz
poz_min_start = total_poz - poz_min + 1
print(poz_min_start)