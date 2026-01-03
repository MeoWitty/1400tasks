massiv = [5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6, 0, 9, 0, 1, 0, 5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6]
summa_chet = 0
for i in range(1, 32, 2):
    summa_chet += massiv[i]
print(summa_chet)