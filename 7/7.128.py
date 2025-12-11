nomer_7 = 0
i = 1
while True:
    b = int(input())
    if b == 1000:
        break
    if b % 10 == 7 and nomer_7 == 0:
        nomer_7 = i
    i += 1
print(nomer_7)