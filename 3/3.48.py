y = float(input("Введите угол y (0 ≤ y < 360): "))
h = int(y // 30)
m = int(y % 30 * 2)
print(h, m)