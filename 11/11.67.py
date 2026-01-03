massiv = [3, 4, 2, 5, 3, 4, 2, 5, 3, 4]
summa_chet = 0
summa_nechet = 0
for i in range(0, len(massiv)):
    if i % 2 == 0:
        summa_chet += massiv[i]
    else:
        summa_nechet += massiv[i]
if summa_chet > summa_nechet:
    print("Na chetnoi storone bolshe")
else:
    print("Na nechetnoi storone bolshe")