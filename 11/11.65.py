massiv = [5, 25, 12, 30, 7, 18, 21, 15, 22, 6]
# a)
summa_bolshe20 = 0
for element in massiv:
    if element > 20:
        summa_bolshe20 += element
if summa_bolshe20 > 100:
    print("Verno")
else:
    print("Ne verno")

# б)
summa_menshe50 = 0
for element in massiv:
    if element < 50:
        summa_menshe50 += element
if summa_menshe50 % 2 == 0:
    print("Verno")
else:
    print("Ne verno")