m = int(input())
min_dlina = m
tek_dlina = 0
for i in range(m):
    chislo = int(input())
    if chislo == 1:
        tek_dlina += 1
    else:
        if 0 < tek_dlina < min_dlina:
            min_dlina = tek_dlina
        tek_dlina = 0
if 0 < tek_dlina < min_dlina:
    min_dlina = tek_dlina
if min_dlina == m:
    print(0)
else:
    print(min_dlina)