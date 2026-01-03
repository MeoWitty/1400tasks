massiv = [5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6, 0, 9, 0, 1, 0, 5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6]
# a)
summa1 = 0
summa2 = 0
for i in range(0, 15):
    summa1 += massiv[i]
for i in range(15, 30):
    summa2 += massiv[i]
if summa1 > summa2:
    print("Pervaya polovina")
else:
    print("Vtoraya polovina")

# б)
dekada1 = sum(massiv[0:10])
dekada2 = sum(massiv[10:20])
dekada3 = sum(massiv[20:30])
if dekada1 > dekada2 and dekada1 > dekada3:
    print("Pervaya dekada")
elif dekada2 > dekada1 and dekada2 > dekada3:
    print("Vtoraya dekada")
else:
    print("Tretiya dekada")