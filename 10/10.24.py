import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)

# Проверяем что ладья на (a,b) не угрожает полю (c,d)
while abs(a - c) == 0 or abs(b - d) == 0:
    c = random.randint(1, 8)
    d = random.randint(1, 8)

print(f"Ladya na ({a},{b})")
print(f"Pole ({c},{d}) ne ugrozhaem")

import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)

# Проверяем что слон на (a,b) не угрожает полю (c,d)
while abs(a - c) == abs(b - d):
    c = random.randint(1, 8)
    d = random.randint(1, 8)

print(f"Slon na ({a},{b})")
print(f"Pole ({c},{d}) ne ugrozhaem")

import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)

# Проверяем что король может за один ход попасть на (c,d)
while abs(a - c) > 1 or abs(b - d) > 1:
    c = random.randint(1, 8)
    d = random.randint(1, 8)

print(f"Korol na ({a},{b})")
print(f"Mohet popast na ({c},{d}) za odin hod")

import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)

# Проверяем что ферзь на (a,b) не угрожает полю (c,d)
while (abs(a - c) == 0 or abs(b - d) == 0) or (abs(a - c) == abs(b - d)):
    c = random.randint(1, 8)
    d = random.randint(1, 8)

print(f"Ferz na ({a},{b})")
print(f"Pole ({c},{d}) ne ugrozhaem")

