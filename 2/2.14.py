import math

print("\n2.14. Нахождение гипотенузы прямоугольного треугольника")
a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))
hypotenuse = math.sqrt(a ** 2 + b ** 2)
print(f"Гипотенуза треугольника: {hypotenuse:.2f}")
