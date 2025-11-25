# а
a = 0
b = 1
while b - a > 0.001:
    x = (a + b) / 2
    if (x**4 + 2*x**3 - x - 1) * (a**4 + 2*a**3 - a - 1) < 0:
        b = x
    else:
        a = x
print((a + b) / 2)

# б
a = 1
b = 1.5
while b - a > 0.001:
    x = (a + b) / 2
    if (x**3 - 0.2*x**2 - 0.2*x - 1.2) * (a**3 - 0.2*a**2 - 0.2*a - 1.2) < 0:
        b = x
    else:
        a = x
print((a + b) / 2)