import math
a = float(input("Введите первое основание a: "))
b = float(input("Введите второе основание b: "))
h = float(input("Введите высоту h: "))
c = math.sqrt(h**2 + ((a - b)/2)**2)
print("Периметр трапеции: " + str (a + b + 2 * c))