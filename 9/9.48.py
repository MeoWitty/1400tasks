# 1)
n = int(input())
d = 2
while n > 1:
    if n % d == 0:
        print(d)
        while n % d == 0:
            n //= d
    d += 1

# 2)
n = int(input())
d = 2
while n > 1:
    while n % d == 0:
        print(d)
        n //= d
    d += 1