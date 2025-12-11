n = int(input())
ubyvanie = True
pred = int(input())
for i in range(2, n + 1):
    tek = int(input())
    if tek > pred:
        ubyvanie = False
        break
    pred = tek
print(ubyvanie)