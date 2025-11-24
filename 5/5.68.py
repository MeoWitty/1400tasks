n = int(input())
summa = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    summa += factorial
print(summa)