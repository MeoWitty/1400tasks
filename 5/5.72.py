import math

# a
n = int(input())
summa_obsh = 0
for i in range(1, n + 1):
    summa_sinusov = 0
    for j in range(1, i + 1):
        summa_sinusov += math.sin(j)
    summa_obsh += 1 / summa_sinusov
print(summa_obsh)

# б
n = int(input())
result = math.sqrt(2)
for i in range(2, n + 1):
    result = math.sqrt(2 + result)
print(result)

# в
n = int(input())
summa_obsh = 0
for i in range(1, n + 1):
    summa_cos = 0
    for j in range(1, i + 1):
        summa_cos += math.cos(j)
    summa_obsh += math.cos(summa_cos)
print(summa_obsh)

# г
n = int(input())
summa_obsh = 0
for i in range(1, n + 1):
    summa_sin = 0
    for j in range(1, 2 * i + 1):
        summa_sin += math.sin(j)
    summa_obsh += math.sin(summa_sin)
print(summa_obsh)

# д
n = int(input())
result = math.sqrt(3 * n)
for i in range(n - 1, 0, -1):
    result = math.sqrt(3 * i + result)
print(result)