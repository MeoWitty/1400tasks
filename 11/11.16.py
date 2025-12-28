# a) арифметическая прогрессия
a1 = int(input())
d = int(input())
massiv = []
for i in range(10):
    massiv.append(a1 + i*d)
for element in massiv:
    print(element)

# б) геометрическая прогрессия
b1 = int(input())
q = int(input())
massiv = []
for i in range(20):
    massiv.append(b1 * (q**i))
for element in massiv:
    print(element)