import math

print("\n2.15. Нахождение площади кольца")
R = float(input("Введите внешний радиус кольца: "))
r = float(input("Введите внутренний радиус кольца: "))
ring_area = math.pi * (R ** 2 - r ** 2)
print(f"Площадь кольца: {ring_area:.2f}")
