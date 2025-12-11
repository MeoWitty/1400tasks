# 1 случай
count_pyaterok = 0
vstrechena_dvoika = False
for i in range(20):
    ocenka = int(input())
    if not vstrechena_dvoika:
        if ocenka == 2:
            vstrechena_dvoika = True
    else:
        if ocenka == 5:
            count_pyaterok += 1
print(count_pyaterok)

# 2 случай
count_pyaterok = 0
vstrechena_dvoika = False
for i in range(20):
    ocenka = int(input())
    if ocenka == 2:
        vstrechena_dvoika = True
    elif vstrechena_dvoika and ocenka == 5:
        count_pyaterok += 1
print(count_pyaterok)