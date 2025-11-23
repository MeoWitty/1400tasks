n = int(input())
d1, d2, d3, d4 = n // 1000, n // 100 % 10, n // 10 % 10, n % 10
print(d1 == d4 and d2 == d3)