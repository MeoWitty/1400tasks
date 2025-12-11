n = int(input())
nomer_poslednego = 0
for i in range(1, n + 1):
    b = int(input())
    if b < 0:
        nomer_poslednego = i
print(nomer_poslednego)