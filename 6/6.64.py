n = int(input())
kupyury = [64, 32, 16, 8, 4, 2, 1]
for k in kupyury:
    count = n // k
    if count > 0:
        print(k, "-", count)
        n %= k