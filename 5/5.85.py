a = int(input())
b = int(input())
summa = 0
for i in range(a, b + 1):
    if i % 4 == 0:
        summa += i
print(summa)