summa = 0
for i in range(30, 100):
    if i % 3 == 0 and (i % 10 == 2 or i % 10 == 4 or i % 10 == 8):
        summa += i
print(summa)