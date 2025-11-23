k = int(input())
if k % 10 == 1 and k % 100 != 11:
    print(f"мы нашли {k} гриб")
elif 2 <= k % 10 <= 4 and (k % 100 < 10 or k % 100 >= 20):
    print(f"мы нашли {k} гриба")
else:
    print(f"мы нашли {k} грибов")