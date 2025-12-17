import random

masti = ["piki", "chervi", "bubny", "trefy"]
karty = ["6", "7", "8", "9", "10", "Valet", "Dama", "Korol", "Tuz"]

igrok1_pobed = 0
igrok2_pobed = 0

n = int(input("Skolko raz igraem? "))

for i in range(n):
    mast1 = random.choice(masti)
    karta1 = random.choice(karty)
    mast2 = random.choice(masti)
    karta2 = random.choice(karty)
    indeks1 = karty.index(karta1)
    indeks2 = karty.index(karta2)
    if indeks1 > indeks2:
        igrok1_pobed += 1
    elif indeks2 > indeks1:
        igrok2_pobed += 1
    else:
        indeks_mast1 = masti.index(mast1)
        indeks_mast2 = masti.index(mast2)
        if indeks_mast1 < indeks_mast2:
            igrok1_pobed += 1
        else:
            igrok2_pobed += 1

print(f"Schet: Igrok 1 - {igrok1_pobed}, Igrok 2 - {igrok2_pobed}")
if igrok1_pobed > igrok2_pobed:
    print("Pobedil Igrok 1!")
elif igrok2_pobed > igrok1_pobed:
    print("Pobedil Igrok 2!")
else:
    print("Nichya!")