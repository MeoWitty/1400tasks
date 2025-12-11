n = int(input())
nomer_pobedy = 0
nomer_porazheniya = 0
for i in range(1, n+1):
    mesto = int(input())
    if mesto == 1 and nomer_pobedy == 0:
        nomer_pobedy = i
    if mesto == n and nomer_porazheniya == 0:
        nomer_porazheniya = i
if nomer_pobedy < nomer_porazheniya:
    print("Да")
else:
    print("Нет")