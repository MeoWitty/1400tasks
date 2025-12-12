# а
for vid in range(5):
    cena = int(input())
    sum_vid = 0
    for den in range(6):
        kol = int(input())
        sum_vid += cena * kol
    print(sum_vid)

# б
for den in range(6):
    sum_den = 0
    for vid in range(5):
        cena = int(input())
        kol = int(input())
        sum_den += cena * kol
    print(sum_den)