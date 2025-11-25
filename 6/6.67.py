a = int(input())
b = int(input())
x, y = a, b
while y != 0:
    x, y = y, x % y
nok = a * b // x
print(nok)