x = 2
summa = 1
znak = -1
stepen = 1
for i in range(2, 12):
    chislitel = i
    znamenatel = i + 3
    summa += znak * (chislitel / znamenatel) * (x ** stepen)
    znak = -znak
    stepen += 1
print(summa)