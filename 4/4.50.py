n = int(input())
d1, d2 = n // 10, n % 10
print(4 in (d1, d2) or 7 in (d1, d2))
print(3 in (d1, d2) or 6 in (d1, d2) or 9 in (d1, d2))