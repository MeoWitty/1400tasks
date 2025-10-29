import math
x = float(input())
k = x**2 if math.sin(x) < 0 else abs(x)
f = k * x if k < x else k + x
print(f)