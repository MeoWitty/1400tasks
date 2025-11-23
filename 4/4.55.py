n = int(input())
d1, d2, d3, d4 = n // 1000, n // 100 % 10, n // 10 % 10, n % 10
digits = (d1, d2, d3, d4)
print(2 in digits or 7 in digits)
print(3 in digits or 6 in digits or 9 in digits)