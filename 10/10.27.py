import random

vsego = 10000
vnutri = 0

for i in range(vsego):
    x = random.uniform(0, 3.14159)  # от 0 до pi
    y = random.uniform(0, 1)  # от 0 до 1

    if y <= 0.5 * abs(3.14159 / 2 - x):  # полусинусоида
        vnutri += 1

ploshad = 3.14159 * (vnutri / vsego)
print(f"Priblizitelnaya ploshad: {ploshad}")

import random

vsego = 10000
vnutri = 0

for i in range(vsego):
    x = random.uniform(0, 3)
    y = random.uniform(0, 9)  # y = x^2, при x=3, y=9

    if y <= x * x:  # под параболой
        vnutri += 1

ploshad = 3 * 9 * (vnutri / vsego)
print(f"Priblizitelnaya ploshad: {ploshad}")

