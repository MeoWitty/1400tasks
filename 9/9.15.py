# а
for magazin in range(3):
    max_d = 0
    max_den = 0
    for den in range(10):
        d = int(input())
        if d > max_d:
            max_d = d
            max_den = den + 1
    print(max_den)

# б
for den in range(10):
    max_d = 0
    max_mag = 0
    for magazin in range(3):
        d = int(input())
        if d > max_d:
            max_d = d
            max_mag = magazin + 1
    print(max_mag)