import random

# a)
for i in range(10):
    print(random.randint(0, 10))

# б)
k = int(input())
a = int(input())
for i in range(k):
    print(random.randint(0, a))

# в)
for i in range(20):
    print(random.randint(10, 20))

# г)
k = int(input())
a = int(input())
for i in range(k):
    print(random.randint(-10, a))

# д)
a = int(input())
b = int(input())
k = random.randint(1, 15)
for i in range(k):
    print(random.randint(a, b))