n = int(input())
for s in range(n, n + 11):
    ost = s
    for k in [64, 32, 16, 8, 4, 2, 1]:
        kol = ost // k
        ost = ost % k
        print(kol, end=' ')
    print()