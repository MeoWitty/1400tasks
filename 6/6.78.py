n = int(input())
temp = n
vozrast = True
pred = 10
while temp > 0:
    tek = temp % 10
    if tek >= pred:
        vozrast = False
        break
    pred = tek
    temp //= 10
print(vozrast)