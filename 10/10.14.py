import random

igrok1_sum = 0
igrok2_sum = 0
igrok3_sum = 0

for i in range(3):
    igrok1_sum += random.randint(1, 6)
for i in range(3):
    igrok2_sum += random.randint(1, 6)
for i in range(3):
    igrok3_sum += random.randint(1, 6)

print("Summa igrok 1:", igrok1_sum)
print("Summa igrok 2:", igrok2_sum)
print("Summa igrok 3:", igrok3_sum)

if igrok1_sum > igrok2_sum and igrok1_sum > igrok3_sum:
    print("Igrok 1 pobedil")
elif igrok2_sum > igrok1_sum and igrok2_sum > igrok3_sum:
    print("Igrok 2 pobedil")
elif igrok3_sum > igrok1_sum and igrok3_sum > igrok2_sum:
    print("Igrok 3 pobedil")
else:
    print("Net pobeditelya (nicheya)")