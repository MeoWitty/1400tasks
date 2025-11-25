a = int(input())
b = int(input())
while a > 0 and b > 0:
    if a >= b:
        count = a // b
        print(f"Квадрат {b}x{b}: {count} шт.")
        a = a % b
    else:
        count = b // a
        print(f"Квадрат {a}x{a}: {count} шт.")
        b = b % a