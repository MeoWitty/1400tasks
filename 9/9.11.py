# а
for rabotnik in range(12):
    max_z = 0
    max_mesac = 0
    for mesac in range(3):
        z = int(input())
        if z > max_z:
            max_z = z
            max_mesac = mesac + 1
    print(max_mesac)

# б
for mesac in range(3):
    max_z = 0
    max_rabotnik = 0
    for rabotnik in range(12):
        z = int(input())
        if z > max_z:
            max_z = z
            max_rabotnik = rabotnik + 1
    print(max_rabotnik)