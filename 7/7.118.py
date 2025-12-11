n = int(input())

# а
nomer_poslednego = 0
for i in range(1, n + 1):
    a = int(input())
    if a == 10:
        nomer_poslednego = i
print(nomer_poslednego)

# б
nomer_pervogo = 0
for i in range(1, n + 1):
    a = int(input())
    if a == 10 and nomer_pervogo == 0:
        nomer_pervogo = i
print(nomer_pervogo)