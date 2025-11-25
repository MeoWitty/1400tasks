ploshad = 100
uroj = 20
obshiy_uroj = 0
god = 1

# а
while uroj <= 22:
    uroj *= 1.02
    god += 1
print(god)

# б
ploshad = 100
god = 1
while ploshad <= 120:
    ploshad *= 1.05
    god += 1
print(god)

# в
ploshad = 100
uroj = 20
obshiy_uroj = 0
god = 1
while obshiy_uroj <= 800:
    obshiy_uroj += ploshad * uroj
    ploshad *= 1.05
    uroj *= 1.02
    god += 1
print(god)