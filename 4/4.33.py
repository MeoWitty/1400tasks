n = int(input())
a_num = int(input())
a, b, c = n // 100, n // 10 % 10, n % 10
s, p = a + b + c, a * b * c
print(s > 9, p > 99, p > a_num, s % 5 == 0, s % a_num == 0)