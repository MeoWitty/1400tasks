import math
x = float(input())
k = x**2 if math.sin(x) >= 0 else abs(x)
f = abs(x) if x < k else k * x
print(f)