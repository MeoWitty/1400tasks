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
if count_malch > 0:
    print("Sredniy rost malchikov:", summa_malch / count_malch)
if count_dev > 0:
    print("Sredniy rost devochek:", summa_dev / count_dev)