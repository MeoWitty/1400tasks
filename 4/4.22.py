m, n = int(input()), int(input())
print(m//n if m % n == 0 else f"{m} на {n} нацело не делится")