for n in range(100, 1000):
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    if a != b and a != c and b != c:
        print(n)