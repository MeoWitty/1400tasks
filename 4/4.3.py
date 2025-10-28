import math
x = float(input())
y = math.sin(x**2) if x > 0 else 1 - 2 * math.sin(x)**2
print(y)