n = int(input())
a = int(input())
n1, n2, n3, n4 = n // 1000, n // 100 % 10, n // 10 % 10, n % 10
s, p = n1 + n2 + n3 + n4, n1 * n2 * n3 * n4
print(n1 + n2 == n3 + n4, s % 3 == 0, p % 4 == 0, p % a == 0)