# a
uroj = 20
for god in range(2, 9):
    uroj *= 1.02
    print(uroj)

# б
ploshad = 100
for god in range(4, 8):
    ploshad *= 1.05
    print(ploshad)

# в
ploshad = 100
uroj = 20
obshiy_uroj = 0
for god in range(1, 7):
    obshiy_uroj += ploshad * uroj
    ploshad *= 1.05
    uroj *= 1.02
print(obshiy_uroj)