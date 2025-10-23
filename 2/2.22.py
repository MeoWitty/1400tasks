import math
x = float(input("Введите значение x: ")) ; abs_x = abs(x)
y = float(input("Введите значение y: ")) ; abs_y = abs(y)
arifmiticheskoe = (x + y) / 2
geometricheskoe = math.sqrt(abs_x * abs_y)
print("Среднее арифметическое модулей:", arifmiticheskoe)
print("Среднее геометрическое модулей:", geometricheskoe)