import math
a = float(input("Введите a: "))
b = float(input("Введите b: "))
numerator_x = (2 / (a ** 2 + 25)) + b
denominator_x = math.sqrt(b + (a + b) / 2)
x = numerator_x / denominator_x
y = (abs(a) + 2 * math.sin(b)) / (5.5 * a)
print(x)
print(y)
