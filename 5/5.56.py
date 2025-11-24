import math
shag = 0.001
x = 0
ploshad = 0
while x <= math.pi:
    y = math.sin(x)
    ploshad += y * shag
    x += shag
print(ploshad)