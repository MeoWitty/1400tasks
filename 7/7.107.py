n = int(input())
m = int(input())
summa = 0
count = 0
for i in range(n):
    a = int(input())
    if a > m:
        summa += a
        count += 1
print(summa / count)