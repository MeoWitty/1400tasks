massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
summa_pol = 0
summa_otr = 0
for element in massiv:
    if element > 0:
        summa_pol += element
    elif element < 0:
        summa_otr += abs(element)
if summa_otr != 0:
    chastnoe = summa_pol / summa_otr
    print(chastnoe)
else:
    print("Delenie na nol")