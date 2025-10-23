import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
c = math.sqrt((x1-x3)**2 + (y1-y3)**2)
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(p * 2)
print(s)