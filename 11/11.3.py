import random
# a)
massiv = []
for i in range(14):
    massiv.append(random.random())
for element in massiv:
    print(element)

# б)
massiv = []
for i in range(14):
    massiv.append(random.uniform(22, 23))
for element in massiv:
    print(element)

# в)
massiv = []
for i in range(14):
    massiv.append(random.uniform(0, 10))
for element in massiv:
    print(element)

# г)
massiv = []
for i in range(14):
    massiv.append(random.uniform(-50, 50))
for element in massiv:
    print(element)

# д)
massiv = []
for i in range(14):
    massiv.append(random.randint(0, 10))
for element in massiv:
    print(element)