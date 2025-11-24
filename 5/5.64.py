chislo = int(input())
obratnoe = 0
while chislo > 0:
    obratnoe = obratnoe * 10 + chislo % 10
    chislo //= 10
print(obratnoe)