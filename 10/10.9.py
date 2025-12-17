import random

kol_resh = 0
kol_orel = 0
for i in range(100):
    moneta = random.randint(0, 1)
    if moneta == 0:
        kol_resh += 1
    else:
        kol_orel += 1
print(kol_resh / 100, kol_orel / 100)

kol_resh = 0
kol_orel = 0
for i in range(1000):
    moneta = random.randint(0, 1)
    if moneta == 0:
        kol_resh += 1
    else:
        kol_orel += 1
print(kol_resh / 1000, kol_orel / 1000)