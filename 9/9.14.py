max_doxod = 0
max_magazin = 0
max_den = 0
for magazin in range(3):
    doxod_mag = 0
    for den in range(10):
        d = int(input())
        doxod_mag += d
        if d > max_doxod:
            max_doxod = d
            max_magazin = magazin + 1
            max_den = den + 1
    if doxod_mag > max_doxod:
        max_doxod = doxod_mag
        max_magazin = magazin + 1
print(max_magazin, max_den, max_doxod)