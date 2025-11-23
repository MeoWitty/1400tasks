n = int(input())
b = int(input())
d1, d2, d3, d4 = n // 1000, n // 100 % 10, n // 10 % 10, n % 10
print(4 in (d1, d2, d3, d4), b in (d1, d2, d3, d4))