import random

# a)
for i in range(8):
    print(random.random())

# б)
k = int(input())
for i in range(k):
    print(random.random())

# в)
for i in range(15):
    print(random.uniform(25, 26))

# г)
for i in range(20):
    print(random.uniform(0, 15))

# д)
a = int(input())
b = int(input())
k = random.randint(1, a)
for i in range(k):
    print(random.uniform(0, b))

# е)
for i in range(10):
    print(random.uniform(-40, 40))

# ж)
m = int(input())
a = int(input())
b = int(input())
k = random.randint(1, m)
for i in range(k):
    print(random.uniform(a, b))