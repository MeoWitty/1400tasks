massiv = [150, 160, -170, -165, 155, -175, 180, -172, 168, -162, 158, -152, 148, -145, 140, -135, 130, -125, 120, -115, 110, -105]
summa_malch = 0
count_malch = 0
summa_dev = 0
count_dev = 0
for element in massiv:
    if element < 0:
        summa_malch += abs(element)
        count_malch += 1
    else:
        summa_dev += element
        count_dev += 1
sred_malch = summa_malch / count_malch
sred_dev = summa_dev / count_dev
if sred_malch - sred_dev > 10:
    print("Verno")
else:
    print("Ne verno")