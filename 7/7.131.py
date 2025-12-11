odinakovyh = 0
pred = int(input())
for i in range(19):
    tek = int(input())
    if tek == pred:
        odinakovyh += 1
    else:
        pred = tek
print(odinakovyh)