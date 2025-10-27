for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if b * 100 + a * 10 + c == 546:
                x = a * 100 + b * 10 + c
                print("Число x =", x)
                break