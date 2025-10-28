for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if c * 100 + b * 10 + a == 654:
                print("x =", a * 100 + b * 10 + c)
                exit()