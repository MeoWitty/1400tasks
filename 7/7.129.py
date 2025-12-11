nomer_kratn_7 = 0
i = 1
while True:
    chislo = int(input())
    if chislo == -1:
        break
    if chislo % 7 == 0 and nomer_kratn_7 == 0:
        nomer_kratn_7 = i
    i += 1
print(nomer_kratn_7)