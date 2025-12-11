odinakovye = True
pred = int(input())
while True:
    tek = int(input())
    if tek < 0:
        break
    if tek != pred:
        odinakovye = False
        break
    pred = tek
print(odinakovye)