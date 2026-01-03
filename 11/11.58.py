massiv = [5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2]
summa_obyaz = sum(massiv[0:6])
summa_proizv = sum(massiv[6:18])
if summa_obyaz > summa_proizv:
    print("Luchshe obyazatelnaya programma")
else:
    print("Luchshe proizvolnaya programma")