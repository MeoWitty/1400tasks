print("Дана формула линнейного уравнения : ax+b=0 (a не равно нулю)")
print("Введите коэфициент (a) ")
a = int(input())
print("Введите коэфициент (b) ")
b = int(input())
if a == 0:
    if b == 0:
        print("x - любое число")
    else:
        print("Решений нет")
else:
    x = -b / a
    print(f"x = {x}")
