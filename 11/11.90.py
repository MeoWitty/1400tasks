massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
summa_pol = 0
count_pol = 0
summa_otr = 0
count_otr = 0
for element in massiv:
    if element > 0:
        summa_pol += element
        count_pol += 1
    elif element < 0:
        summa_otr += element
        count_otr += 1
if count_pol > 0:
    print("Srednee polozhitelnykh:", summa_pol / count_pol)
if count_otr > 0:
    print("Srednee otritsatelnykh:", summa_otr / count_otr)