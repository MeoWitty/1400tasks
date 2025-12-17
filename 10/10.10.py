import random

print("Chet (vvedite 2) ili nechet (vvedite 1)?")
otvet = int(input())
comp = random.randint(1, 2)
print("Computer vybral:", comp)
if otvet == comp:
    print("Ugadal!")
else:
    print("Ne ugadal.")