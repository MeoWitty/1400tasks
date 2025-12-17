import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)
e = random.randint(1, 8)
f = random.randint(1, 8)

# Белая ладья не должна попасть под удар черной ладьи
# и должна иметь путь на (e,f)
while (a == c or b == d) or not ((a == e or b == f) and not (c == e and d == f)):
    e = random.randint(1, 8)
    f = random.randint(1, 8)

print(f"Belaya ladya na ({a},{b})")
print(f"Chernaya ladya na ({c},{d})")
print(f"Belaya mohet poyti na ({e},{f}) bez opasnosti")

import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)
e = random.randint(1, 8)
f = random.randint(1, 8)

# Белая ладья не должна попасть под удар черного ферзя
# и должна иметь путь на (e,f)
while (a == c or b == d or abs(a - c) == abs(b - d)) or not ((a == e or b == f) and not (c == e or d == f or abs(c - e) == abs(d - f))):
    e = random.randint(1, 8)
    f = random.randint(1, 8)

print(f"Belaya ladya na ({a},{b})")
print(f"Chernыy ferz na ({c},{d})")
print(f"Belaya mohet poyti na ({e},{f}) bez opasnosti")

