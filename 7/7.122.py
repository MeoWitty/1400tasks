n = int(input())
nomer_poslednego = 0
for i in range(1, n + 1):
    x = int(input())
    if x % 10 == 2:
        nomer_poslednego = i
if nomer_poslednego > 0:
    print(nomer_poslednego)
else:
    print("Нет таких")