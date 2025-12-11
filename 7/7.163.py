n = int(input())
min_vremya = float('inf')
nomer_poslednego = 0
spisok_t = []
for i in range(n):
    t = float(input())
    spisok_t.append(t)
    if t < min_vremya:
        min_vremya = t
        nomer_poslednego = i + 1
    elif t == min_vremya:
        nomer_poslednego = i + 1
print(nomer_poslednego)