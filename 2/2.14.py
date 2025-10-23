import math
a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))
hypotenuse = math.sqrt(a ** 2 + b ** 2)
print("Гипотенуза треугольника равна: " + str(hypotenuse))
