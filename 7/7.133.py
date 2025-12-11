odinakovyh = 0
pred = float(input())
while True:
    tek = float(input())
    if tek == 1000:
        break
    if tek == pred:
        odinakovyh += 1
    else:
        pred = tek
print(odinakovyh)