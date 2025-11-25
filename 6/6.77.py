n = int(input())

# а
temp = n
cifra = n % 10
odinakovie = True
while temp > 0:
    if temp % 10 != cifra:
        odinakovie = False
        break
    temp //= 10
print(odinakovie)

# б
temp = n
pred = -1
est_odinakovie = False
while temp > 0:
    tek = temp % 10
    if tek == pred:
        est_odinakovie = True
        break
    pred = tek
    temp //= 10
print(est_odinakovie)