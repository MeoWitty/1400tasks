shag = 0.001
x = 0
ploshad = 0
while x <= 2:
    y = 0.3 * (x - 1) ** 2 + 3
    if 2 <= y <= 4:
        ploshad += y * shag
    x += shag
print(ploshad)