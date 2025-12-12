n = 1
while True:
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if a + b == n:
                count += 1
    if count >= 2:
        print(n)
        break
    n += 1