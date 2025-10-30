n = int(input())
a = int(input())
s = n // 10 + n % 10
print(s % 3 == 0, s % a == 0)