import random

# a)
a = random.randint(0, 2)
b = random.randint(0, 3)
while b == a:
    b = random.randint(0, 3)
print(a, b)

# б)
a = random.randint(1, 3)
b = random.randint(0, 3)
c = random.randint(1, 4)
while b == a:
    b = random.randint(0, 3)
while c == a or c == b:
    c = random.randint(1, 4)
print(a, b, c)

# в)
spisok = []
for i in range(7):
    spisok.append(2)
for i in range(8):
    spisok.append(3)
random.shuffle(spisok)
for chislo in spisok:
    print(chislo)