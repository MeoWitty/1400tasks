n = int(input())
num = int(input())
d1, d2, d3 = n // 100, n // 10 % 10, n % 10
print(6 in (d1, d2, d3), num in (d1, d2, d3))