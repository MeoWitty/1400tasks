import math

print("\n2.17. Нахождение периметра равнобедренной трапеции")
a = float(input("Введите меньшее основание трапеции: "))
b = float(input("Введите большее основание трапеции: "))
h = float(input("Введите высоту трапеции: "))
side = math.sqrt(h ** 2 + ((b - a) / 2) ** 2)
trapezoid_perimeter = a + b + 2 * side
print(f"Периметр трапеции: {trapezoid_perimeter:.2f}")
