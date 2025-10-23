import math
x1 = float(input("введите первый x: "))
y1 = float(input("введите первый y: "))
x2 = float(input("введите второй x: "))
y2 = float(input("введите второй y: "))
print("Расстояние между точками:",str(math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)))