n = int(input())
max_chislo = float('-inf')
min_chislo = float('inf')
nomer_poslednego_max = 0
nomer_poslednego_min = 0
for i in range(1, n+1):
    a = int(input())
    if a >= max_chislo:
        max_chislo = a
        nomer_poslednego_max = i
    if a <= min_chislo:
        min_chislo = a
        nomer_poslednego_min = i
print(nomer_poslednego_max, nomer_poslednego_min)