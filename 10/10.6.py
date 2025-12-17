import random

kol_ed = 0
kol_nul = 0
for i in range(50):
    chislo = random.randint(0, 1)
    if chislo == 1:
        kol_ed += 1
    else:
        kol_nul += 1
print(kol_ed)
print(kol_nul)