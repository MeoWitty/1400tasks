n = int(input())
p = float(input())
summa = 0
for i in range(n):
    b = float(input())
    if b > p:
        summa += b
print(summa)