import math
x = float(input("Введите x: "))
y = float(input("Введите y: "))
numerator = x + (2 + y) / (x ** 2)
denominator = math.sqrt(y + 1 / math.sqrt(x ** 2 + 10))
z = numerator / denominator
uq = 7.25 * math.sin(x) - abs(y)
print(z)
print(uq)
