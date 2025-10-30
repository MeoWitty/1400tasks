n = int(input())
a, b, c = n // 100, n // 10 % 10, n % 10
print(a > c, a > b, b > c)