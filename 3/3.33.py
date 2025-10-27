n = int(input("Введите число n: "))
for x in range(100, 1000):
    a, b, c = x // 100, x // 10 % 10, x % 10
    if c * 100 + a * 10 + b == n:
        print("Число x =", x)
        break