shag = 0.001
x = 0
ploshad = 0
while x <= 2:
    y = 0.4 * (x + 2) ** 2 + 1
    if y <= 2:
        ploshad += y * shag
    x += shag
print(ploshad)