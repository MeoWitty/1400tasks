n = int(input())
p = int(input())
summa = 0
count = 0
for i in range(n):
    b = int(input())
    if b % p == 0:
        summa += b
        count += 1
print(summa / count)