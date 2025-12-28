import random
N = int(input())
a = int(input())
b = int(input())
massiv = []
for i in range(N):
    massiv.append(random.randint(a, b))
for element in massiv:
    print(element)