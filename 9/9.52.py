p = int(input())
q = int(input())
for d in range(1, q + 1):
    if q % d == 0:
        a = d
        b = p
        while b != 0:
            a, b = b, a % b
        if a == 1:
            print(d)