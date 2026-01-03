massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
# a)
summa = sum(massiv)
if summa % 2 == 0:
    print("Verno")
else:
    print("Ne verno")

# б)
summa_kvadratov = 0
for element in massiv:
    summa_kvadratov += element**2
if summa_kvadratov % 10 == 5:
    print("Verno")
else:
    print("Ne verno")