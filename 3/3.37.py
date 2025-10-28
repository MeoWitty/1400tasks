n = int(input("Введите число n (10 ≤ n ≤ 999, и число десятков в n ≠ 0): "))
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if b * 100 + a * 10 + c == n and n // 10 % 10:
                print("Число x =", a * 100 + b * 10 + c)
                break