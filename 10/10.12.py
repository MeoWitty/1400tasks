import random

igrok1 = random.randint(1, 6)
igrok2 = random.randint(1, 6)
print("Igrok 1:", igrok1)
print("Igrok 2:", igrok2)
if igrok1 > igrok2:
    print("Igrok 1 pobedil")
elif igrok2 > igrok1:
    print("Igrok 2 pobedil")
else:
    print("Nichya")