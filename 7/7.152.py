n = float(input())
nomer_blizhayshego = 0
min_raznica = float('inf')
pred = float('-inf')
for i in range(1, 1000):
    a = float(input())
    if a == 10000:
        break
    if pred <= n <= a:
        raznica1 = abs(n - pred)
        raznica2 = abs(a - n)
        if raznica1 < min_raznica:
            min_raznica = raznica1
            nomer_blizhayshego = i - 1
        if raznica2 < min_raznica:
            min_raznica = raznica2
            nomer_blizhayshego = i
        break
    pred = a
print(nomer_blizhayshego)