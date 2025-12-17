import random

# Выбираем первую кость
kost1_1 = random.randint(0, 6)
kost1_2 = random.randint(0, 6)

# Выбираем вторую кость
kost2_1 = random.randint(0, 6)
kost2_2 = random.randint(0, 6)

print(f"Kost 1: {kost1_1}-{kost1_2}")
print(f"Kost 2: {kost2_1}-{kost2_2}")

# Проверяем можно ли приставить кости друг к другу
if kost1_1 == kost2_1 or kost1_1 == kost2_2 or kost1_2 == kost2_1 or kost1_2 == kost2_2:
    print("Mozhno pristavit")
else:
    print("Nelzya pristavit")