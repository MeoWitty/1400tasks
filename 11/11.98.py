massiv = [100, 200, 150, 300, 250, 120, 180, 220, 190, 210, 170, 130, 140, 160, 180, 200, 220, 240, 260, 280]
sred_stoim = sum(massiv) / len(massiv)
count = 0
for element in massiv:
    if element < sred_stoim:
        count += 1
print(count)