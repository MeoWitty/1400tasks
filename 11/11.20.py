import random

massiv_otvetov = []
pravilno = 0
nepravilno = 0

for i in range(20):
    chislo1 = random.randint(2, 9)
    chislo2 = random.randint(2, 9)
    proizvedenie = chislo1 * chislo2

    print(f"Chto ravno {chislo1} x {chislo2}?")
    otvet = int(input())
    massiv_otvetov.append(otvet)

    if otvet == proizvedenie:
        print("Pravilno!")
        pravilno += 1
    else:
        print(f"Nepravilno! Pravilny otvet: {proizvedenie}")
        nepriavilno += 1

print(f"Pravilnykh otvetov: {pravilno}")
print(f"Nepravilnykh otvetov: {nepravilno}")
print("Vse otvety:", massiv_otvetov)