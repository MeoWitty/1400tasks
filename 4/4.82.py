n = int(input())
if n % 10 == 1 and n % 100 != 11:
    print(f"мне {n} год")
elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
    print(f"мне {n} года")
else:
    print(f"мне {n} лет")