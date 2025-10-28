n = int(input("Введите n (100-999): "))
a, b, c = n // 100, n // 10 % 10, n % 10
x = a * 100 + c * 10 + b
print("x =", x)