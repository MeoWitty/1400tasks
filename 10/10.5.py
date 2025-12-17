import random

for i in range(30):
    chislo = random.randint(0, 5)
    if chislo % 2 != 0:
        print(chislo)