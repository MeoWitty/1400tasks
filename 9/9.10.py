max_zarplata = 0
max_rabotnik = 0
max_sum = 0
for rabotnik in range(12):
    sum_r = 0
    for mesac in range(3):
        z = int(input())
        sum_r += z
        if z > max_zarplata:
            max_zarplata = z
    if sum_r > max_sum:
        max_sum = sum_r
        max_rabotnik = rabotnik + 1
print(max_zarplata)
print(max_rabotnik)