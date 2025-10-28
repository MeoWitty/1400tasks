import math
y = float(input("Введите угол y (в радианах, 0 < y ≤ 2π): "))
h = int(y * 180 / math.pi // 30)
m = int(y * 180 / math.pi % 30 * 2)
print(h, m, m * 6)