s_circle = float(input())
s_square = float(input())
r = (s_circle/3.14159)**0.5
a = s_square**0.5
print("Да" if 2*r <= a else "Нет")
print("Да" if a*2**0.5 <= 2*r else "Нет")