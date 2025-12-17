import random

masti = ["piki", "chervi", "bubny", "trefy"]
karty = ["6", "7", "8", "9", "10", "Valet", "Dama", "Korol", "Tuz"]

# Выбор первого игрока
mast1 = random.choice(masti)
karta1 = random.choice(karty)

# Выбор второго игрока
mast2 = random.choice(masti)
karta2 = random.choice(karty)

print(f"Igrok 1: {karta1} {mast1}")
print(f"Igrok 2: {karta2} {mast2}")

# Определяем старшинство
# Сначала сравниваем достоинства карт
indeks1 = karty.index(karta1)
indeks2 = karty.index(karta2)

if indeks1 > indeks2:
    print("Pobedil igrok 1")
elif indeks2 > indeks1:
    print("Pobedil igrok 2")
else:
    # Если достоинства равны, сравниваем масти
    indeks_mast1 = masti.index(mast1)
    indeks_mast2 = masti.index(mast2)

    if indeks_mast1 < indeks_mast2:  # пики старше
        print("Pobedil igrok 1")
    else:
        print("Pobedil igrok 2")