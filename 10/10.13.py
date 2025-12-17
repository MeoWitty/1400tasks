import random

igrok1_sum = 0
igrok2_sum = 0

for i in range(2):
    igrok1_sum += random.randint(1, 6)
for i in range(2):
    igrok2_sum += random.randint(1, 6)

print("Summa igrok 1:", igrok1_sum)
print("Summa igrok 2:", igrok2_sum)

if igrok1_sum > igrok2_sum:
    print("Igrok 1 pobedil")
elif igrok2_sum > igrok1_sum:
    print("Igrok 2 pobedil")
else:
    print("Nichya")