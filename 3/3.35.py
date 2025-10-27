n = int(input("Введите число n (1 ≤ n ≤ 999): "))
for x in range(100, 1000):
    a, bc = x // 100, x % 100
    if bc * 10 + a == n:
        print("Число x =", x)
        break