import random

chislo1 = random.randint(1, 9)
chislo2 = random.randint(1, 9)
proizvedenie = chislo1 * chislo2

print(f"Chему ravno proizvedenie {chislo1}x{chislo2}?")
otvet = int(input())

if otvet == proizvedenie:
    print("Pravilno!")
else:
    print(f"Nepravilno! Pravilny otvet: {proizvedenie}")

    # Б)
    import random

    pravilno = 0
    nepravilno = 0

    for i in range(20):
        chislo1 = random.randint(1, 9)
        chislo2 = random.randint(1, 9)
        proizvedenie = chislo1 * chislo2

        print(f"Vopros {i + 1}: Chему ravno {chislo1}x{chislo2}?")
        otvet = int(input())

        if otvet == proizvedenie:
            print("Pravilno!")
            pravilno += 1
        else:
            print(f"Nepravilno! Pravilny otvet: {proizvedenie}")
            nepri