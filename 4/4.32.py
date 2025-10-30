n = int(input())
a, b, c = n // 100, n // 10 % 10, n % 10
print(n**2 == a**3 + b**3 + c**3)