m = int(input())
n = int(input())
for x in range(1, m):
    s = 0
    t = x
    while t > 0:
        s += t % 10
        t //= 10
    if s**2 == n:
        print(x)