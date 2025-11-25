n = int(input())
poz = 0
nomer = 0
temp = n
while temp > 0:
    poz += 1
    if temp % 10 == 8:
        nomer = poz
    temp //= 10
print(nomer)