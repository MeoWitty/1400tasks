import random

chastoty = [0, 0, 0, 0, 0, 0]
for i in range(100):
    kubik = random.randint(1, 6)
    chastoty[kubik - 1] += 1

for i in range(6):
    print(f"Chislo {i + 1}: {chastoty[i] / 100}")