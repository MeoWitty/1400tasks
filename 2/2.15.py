import math
R = float(input("Введите внешний радиус кольца: "))
r = float(input("Введите внутренний радиус кольца: "))
ring_area = math.pi * (R ** 2 - r ** 2)
print("Площадь кольца: " + str(ring_area))
