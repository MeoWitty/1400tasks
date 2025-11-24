x = float(input())
n = int(input())
summa = 1
factorial = 1
stepen = 1
for i in range(1, n + 1):
    factorial *= i
    stepen *= x
    summa += stepen / factorial
print(summa)