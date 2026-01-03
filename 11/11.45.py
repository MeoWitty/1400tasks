massiv = [5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6, 0, 9, 0, 1, 0, 5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6]
summa_chet = 0
summa_nechet = 0
for i in range(0, len(massiv)):
    if i % 2 == 0:
        summa_chet += massiv[i]
    else:
        summa_nechet += massiv[i]
if summa_chet > summa_nechet:
    print("Verno")
else:
    print("Ne verno")