n = int(input())

# а
max_summa = float('-inf')
for i in range(n-1):
    x1 = int(input())
    x2 = int(input())
    summa = x1 + x2
    if summa > max_summa:
        max_summa = summa

# б
min_summa = float('inf')
for i in range(n-1):
    x1 = int(input())
    x2 = int(input())
    summa = x1 + x2
    if summa < min_summa:
        min_summa = summa

# в
max_summa = float('-inf')
nomer1 = 0
nomer2 = 0
x_pred = int(input())
for i in range(2, n+1):
    x_tek = int(input())
    summa = x_pred + x_tek
    if summa > max_summa:
        max_summa = summa
        nomer1 = i-1
        nomer2 = i
    x_pred = x_tek
print(nomer1, nomer2)

# г
min_summa = float('inf')
nomer1 = 0
nomer2 = 0
x_pred = int(input())
for i in range(2, n+1):
    x_tek = int(input())
    summa = x_pred + x_tek
    if summa < min_summa:
        min_summa = summa
        nomer1 = i-1
        nomer2 = i
    x_pred = x_tek
print(nomer1, nomer2)