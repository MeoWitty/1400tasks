n = int(input())
max_chislo = float('-inf')
min_chislo = float('inf')
nomer_max = 0
nomer_min = 0
for i in range(1, n+1):
    x = int(input())
    if x > max_chislo:
        max_chislo = x
        nomer_max = i
    if x < min_chislo:
        min_chislo = x
        nomer_min = i
if nomer_max < nomer_min:
    print("Максимальное")
else:
    print("Минимальное")