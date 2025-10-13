import math

print("\n2.18. Вычисление значения функции")
x = float(input("Введите x: "))
y = float(input("Введите y: "))
numerator = x + (2 + y) / (x ** 2)
denominator = math.sqrt(y + 1 / math.sqrt(x ** 2 + 10))
z = numerator / denominator
uq = 7.25 * math.sin(x) - abs(y)
print(f"z = {z:.4f}")
print(f"uq = {uq:.4f}")
