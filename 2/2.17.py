import math
a = float(input("Введите меньшее основание трапеции: "))
b = float(input("Введите большее основание трапеции: "))
h = float(input("Введите высоту трапеции: "))
side = math.sqrt(h ** 2 + ((b - a) / 2) ** 2)
perimeter = a + b + 2 * side
print("Периметр трапеции: " +str(perimeter))
