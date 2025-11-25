a = int(input())
b = int(input())
x, y = a, b
while y != 0:
    x, y = y, x % y
p = a // x
q = b // x
print(p, q)