n = int(input())
a = int(input())
d1, d2 = n // 10, n % 10
print(3 in (d1, d2), a in (d1, d2))