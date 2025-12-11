n = int(input())

# а
max_chislo = float('-inf')
nomer_poslednego_max = 0
for i in range(1, n+1):
    a = int(input())
    if a >= max_chislo:
        max_chislo = a
        nomer_poslednego_max = i
print(nomer_poslednego_max)

# б
min_chislo = float('inf')
nomer_pervogo_min = 0
for i in range(1, n+1):
    a = int(input())
    if a < min_chislo:
        min_chislo = a
        nomer_pervogo_min = i
print(nomer_pervogo_min)