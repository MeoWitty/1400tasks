max_vozrast = 0
min_vozrast = float('inf')
nomer_starshego = 0
nomer_mladshego = 0
i = 1
while True:
    vozrast = int(input())
    if vozrast == 0:
        break
    if vozrast > max_vozrast:
        max_vozrast = vozrast
        nomer_starshego = i
    if vozrast < min_vozrast:
        min_vozrast = vozrast
        nomer_mladshego = i
    i += 1
if nomer_starshego < nomer_mladshego:
    print("Старший")
else:
    print("Младший")