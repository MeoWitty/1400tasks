import random

a = int(input())
b = int(input())
m = random.randint(1, 20)
n = random.randint(1, 20)
for i in range(m):
    print(random.randint(0, b))
for i in range(n):
    print(random.uniform(0, n))