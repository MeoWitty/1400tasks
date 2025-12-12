for n in range(100, 1000):
    prostoe = True
    for i in range(2, n):
        if n % i == 0:
            prostoe = False
            break
    if prostoe:
        print(n)