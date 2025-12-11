n = int(input())
ubyvanie = True
pred = float(input())
for i in range(2, n + 1):
    tek = float(input())
    if tek > pred:
        ubyvanie = False
        break
    pred = tek
print(ubyvanie)