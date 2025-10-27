n = int(input("Введите число n: "))
for x in range(100, 1000):
    a, bc = x // 100, x % 100
    if bc * 10 + a == n:
        print("Число x =", x)
        break