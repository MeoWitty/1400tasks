import random

masti = ["piki", "chervi", "bubny", "trefy"]
karty = ["6", "7", "8", "9", "10", "Valet", "Dama", "Korol", "Tuz"]

mast = random.choice(masti)
karta = random.choice(karty)
print(f"Vybrana {karta} {mast}")