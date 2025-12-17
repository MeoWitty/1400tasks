import random

a = random.randint(1, 8)
b = random.randint(2, 7)  # пешка не на последней горизонтали
c = a  # та же вертикаль
d = b + 1  # на одну клетку вперед

print(f"Belaya peshka na ({a},{b})")
print(f"Mohet popast na ({c},{d}) obychnym hodom")

import random

a = random.randint(2, 7)  # не у края доски
b = random.randint(2, 7)
c = random.choice([a-1, a+1])  # по диагонали
d = b + 1  # вперед

print(f"Belaya peshka na ({a},{b})")
print(f"Mohet bit figurу na ({c},{d})")

import random

a = random.randint(1, 8)
b = random.randint(2, 7)  # пешка не на первой горизонтали
c = a  # та же вертикаль
d = b - 1  # на одну клетку вниз

print(f"Chernaya peshka na ({a},{b})")
print(f"Mohet popast na ({c},{d}) obychnym hodom")

import random

a = random.randint(2, 7)  # не у края доски
b = random.randint(2, 7)
c = random.choice([a-1, a+1])  # по диагонали
d = b - 1  # вниз

print(f"Chernaya peshka na ({a},{b})")
print(f"Mohet bit figurу na ({c},{d})")

import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)

# Проверяем что конь на (a,b) угрожает полю (c,d)
# Конь ходит буквой Г: разница 2 и 1 или 1 и 2
while not ((abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2)):
    c = random.randint(1, 8)
    d = random.randint(1, 8)

print(f"Kon na ({a},{b})")
print(f"Ugrozhaet polyu ({c},{d})")

