import random

masti = ["piki", "chervi", "bubny", "trefy"]
karty = ["6", "7", "8", "9", "10", "Valet", "Dama", "Korol", "Tuz"]


kozyrnaya_mast = random.choice(masti)
print(f"Kozyrnaya mast: {kozyrnaya_mast}")


mast1 = random.choice(masti)
karta1 = random.choice(karty)

mast2 = random.choice(masti)
karta2 = random.choice(karty)

print(f"Igrok 1: {karta1} {mast1}")
print(f"Igrok 2: {karta2} {mast2}")

if mast1 == kozyrnaya_mast and mast2 != kozyrnaya_mast:
    print("Pobedil Igrok 1 (kozyr!)")
elif mast2 == kozyrnaya_mast and mast1 != kozyrnaya_mast:
    print("Pobedil Igrok 2 (kozyr!)")
elif mast1 == kozyrnaya_mast and mast2 == kozyrnaya_mast:
    # Оба козыри, сравниваем достоинства
    indeks1 = karty.index(karta1)
    indeks2 = karty.index(karta2)
    if indeks1 > indeks2:
        print("Pobedil Igrok 1")
    else:
        print("Pobedil Igrok 2")
else:

    indeks1 = karty.index(karta1)
    indeks2 = karty.index(karta2)

    if indeks1 > indeks2:
        print("Pobedil Igrok 1")
    elif indeks2 > indeks1:
        print("Pobedil Igrok 2")
    else:
        indeks_mast1 = masti.index(mast1)
        indeks_mast2 = masti.index(mast2)
        if indeks_mast1 < indeks_mast2:
            print("Pobedil Igrok 1")
        else:
            print("Pobedil Igrok 2")