massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
count_pol = 0
count_otr = 0
for element in massiv:
    if element > 0:
        count_pol += 1
    elif element < 0:
        count_otr += 1
print("Polozhitelnykh:", count_pol)
print("Otritsatelnykh:", count_otr)