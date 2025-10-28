n = int(input("Введите число n: "))
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if (a * 10 + c) * 10 + b == n:
                print("Число x =", a * 100 + b * 10 + c)
                exit()