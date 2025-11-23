n = int(input())
d1, d2, d3 = n // 100, n // 10 % 10, n % 10
print(4 in (d1, d2, d3) or 7 in (d1, d2, d3))
print(3 in (d1, d2, d3) or 6 in (d1, d2, d3) or 9 in (d1, d2, d3))