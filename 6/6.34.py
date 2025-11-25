m = int(input())
n = int(input())
i = 1
while i <= m * n:
    if i % m == 0 or i % n == 0:
        print(i)
    i += 1