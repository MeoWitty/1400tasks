a = float(input())
x = float(input())
e = float(input())
y1 = (x + a / x) / 2
y2 = (y1 + a / y1) / 2
while abs(y2 - y1) > e:
    y1 = y2
    y2 = (y1 + a / y1) / 2
print(y2)