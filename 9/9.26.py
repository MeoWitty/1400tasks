count = 0
n = 2
while count < 100:
    prostoe = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prostoe = False
            break
    if prostoe:
        print(n)
        count += 1
    n += 1