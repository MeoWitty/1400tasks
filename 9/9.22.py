for n in range(200, 501):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 6:
        print(n)