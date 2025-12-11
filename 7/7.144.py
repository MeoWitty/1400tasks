n = int(input())

# а
max_summa = float('-inf')
for i in range(n):
    a = int(input())
    b = int(input())
    summa = a + b
    if summa > max_summa:
        max_summa = summa
print(max_summa)

# б
min_proizv = float('inf')
for i in range(n):
    a = int(input())
    b = int(input())
    proizv = a * b
    if proizv < min_proizv:
        min_proizv = proizv
print(min_proizv)