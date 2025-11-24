n = int(input())
nach = n * (n - 1) + 1
summa = 0
for i in range(n):
    summa += nach
    nach += 2
print(summa)