n = int(input())
odinakovye = True
pred = int(input())
for i in range(2, n + 1):
    tek = int(input())
    if tek != pred:
        odinakovye = False
        break
    pred = tek
print(odinakovye)