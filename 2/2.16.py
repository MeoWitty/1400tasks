import math

print("\n2.16. Нахождение периметра прямоугольного треугольника")
a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))
c = math.sqrt(a ** 2 + b ** 2)
perimeter = a + b + c
print(f"Периметр треугольника: {perimeter:.2f}")
