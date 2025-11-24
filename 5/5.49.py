# a
vklad = 1000
for i in range(1, 11):
    prirast = vklad * 0.02
    print(prirast)
    vklad += prirast

# б
vklad = 1000
for i in range(1, 13):
    vklad *= 1.02
    if i >= 3:
        print(vklad)