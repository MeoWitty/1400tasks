s_circle = float(input())
s_triangle = float(input())
r = (s_circle/3.14159)**0.5
a = (4*s_triangle/3**0.5)**0.5
print("Да" if 2*r <= a*3**0.5/3 else "Нет")
print("Да" if a <= 2*r*3**0.5 else "Нет")